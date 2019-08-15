from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task.schedules import crontab  
from celery.decorators import periodic_task
from django.conf import settings

from .services import *
import json
from datetime import datetime

import sentry_sdk
sentry_url = os.getenv('SENTRY_URL')
sentry_sdk.init(sentry_url)

# Get an instance of a logger
logger = logging.getLogger('django.request')

# set variables
public_url = os.getenv('public_url')
public_url_sendmail = os.getenv('public_url_sendmail')
account_token = os.getenv('account_token')
lej_url = os.getenv('LEJ_URL')

@shared_task
def add(x, y):
    return x + y

@shared_task
def premium_check():
    response = CALL_REQUEST('account', 'get', router=f'/customer/plan/', token=account_token)
    content = json.loads(response.content)
    if content['code'] != 'S001021':
        logger.error('Service /customer/plan/ is broken.')
        return 'Service /customer/plan/ is broken.'
    premium_list = content['data']
    today = datetime.today()
    
    # Extract member
    id_list = []
    for member in premium_list:
        id_list.append(member['customer_id'])
    id_set_list = list(set(id_list))

    # Find latest data for unique customers
    latest_customer_list = []
    for id in id_set_list:
        date_list = [datetime.strptime(x['end_date'], '%Y-%m-%d') for x in premium_list if x['customer_id']==id]
        max_end_date = max(date_list).strftime('%Y-%m-%d')
        customer = next(item for item in premium_list if item['end_date'] == max_end_date and item['customer_id']==id)
        latest_customer_list.append(customer)

    for customer in latest_customer_list:
        end_date = datetime.strptime(customer['end_date'], '%Y-%m-%d')
        date_diff = end_date - today
        date_diff = date_diff.days
        if date_diff == -1:
            # call myself 
            service_customer_id = customer['customer_id']
            data = {
                'service_customer_id': service_customer_id
            }
            response = CALL_REQUEST('self', 'post', router=f'/token_charge/', data=data)
            if not response:
                logger.error(f'Fail to continue the premium service_customer_id {service_customer_id} since transaction service error')
                return 'Error'
            content = json.loads(response.content)
            if content['code'] == 'S003037':
                logger.error(f'Customer no charge token, service_customer_id {service_customer_id}, stop the premium qualification.')
                return 'No token'
            elif content['code'] != 'S003036':
                logger.error(f'Fail to charge with token, service_customer_id {service_customer_id}')
                return 'Fail to charge'
            transaction_id = content['data']['transaction_id']

            # Upate premium privilege via account service
            # 30 days for this return data
            plus_date = 30
            update_period_data = CALCULATE_PREMIUM_VALID_PERIOD(service_customer_id, plus_date)
            update_period_data['transaction_id'] = transaction_id
            response = CALL_REQUEST('account', 'post', router=f'/customer/{service_customer_id}/plan/', data=update_period_data, token=account_token)
            update_result = json.loads(response.content)
            if update_result['code'] != 'S001018':
                logger.error(f'Update customer to premium failed, service_customer_id {service_customer_id}')
                return APIHandler.catch('Update customer to premium failed', code='000')
            if not response:
                logger.error(f'Account service no response while updating premium, service_customer_id {service_customer_id}')
            elif update_result['code'] != 'S001018':
                logger.error(f'Account service failed while updating premium, service_customer_id {service_customer_id}')
        
        
    
    # Check if anyone up-to-date 