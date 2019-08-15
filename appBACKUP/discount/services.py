from django.apps import apps
import requests, logging
from datetime import datetime, timedelta
from payment.gateway_service import UNIQUE_ID_GENERATOR

# Get an instance of a logger
logger = logging.getLogger('django.request')

def GET_ALL_TOPEX_MEMBER():
    SchoolCouponCustomer = apps.get_model('payment', 'SchoolCouponCustomer')
    topex_customers = SchoolCouponCustomer.objects.filter(school_coupon_id='topexcoupon')
    id_list = []
    for customer in topex_customers:
        customer_dict = {'customer_id':customer.customer_id, 'quota':customer.quota}
        id_list.append(customer_dict)
    return id_list

def ACTIVATE_TOPEX_CUSTOMER(customer_id):
    SchoolCouponCustomer = apps.get_model('payment', 'SchoolCouponCustomer')
    quota = 1000
    date_added = datetime.now()
    date_start = datetime.now().date()
    date_end = datetime.now().date() + timedelta(days=730)
    unique_pk = UNIQUE_ID_GENERATOR(SchoolCouponCustomer)
    try:
        new_topex_member = SchoolCouponCustomer.objects.create(
            pk = unique_pk,
            school_coupon_id = 'topexcoupon',
            customer_id  = customer_id,
            quota = quota,
            date_end = date_end,
            date_added = date_added,
            date_start = date_start,
        )
    except:
        return False
    return new_topex_member.id

def REMOVE_TOPEX_CUSTOMER(customer_id):
    SchoolCouponCustomer = apps.get_model('payment', 'SchoolCouponCustomer')
    try:
        customer_list = SchoolCouponCustomer.objects.filter(customer_id = customer_id)
        for customer in customer_list:
            customer.delete()
        return 'Success'
    except:
        return 'Fail'

def CHANGE_TOPEX_QUOTA(customer_id, quota):
    SchoolCouponCustomer = apps.get_model('payment', 'SchoolCouponCustomer')
    try:
        customer_list = SchoolCouponCustomer.objects.filter(customer_id = customer_id)
        for customer in customer_list:
            customer.quota = quota
            customer.date_updated = datetime.now()
            customer.save()
        return 'Success'
    except:
        return 'Fail'

def ECREDIT_VALUE_CONTROL(customer_id, change_point, add_minus, price_prefix='SGD', transaction_id="", description=""):
    try:
        EcreditHistories = apps.get_model('payment', 'EcreditHistories')
        unique_pk = UNIQUE_ID_GENERATOR(EcreditHistories)
        EcreditHistories.objects.create(
            pk = unique_pk,
            customer_id  = customer_id,
            change_point = int(change_point),
            add_minus = add_minus,
            description = description,
            price_prefix = price_prefix,
            transaction_id = transaction_id
        )
        return True
    except:
        return False