import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import requests
from helper.helper import APIHandler
import logging, random, string

from payment.serializers import *
from .models import CurrencyLists, AwardCouponHistories
from .services import *
from .gateway_service import *

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

'''Save data below''' 
class StoreGuestTempInfo(APIView):
    def post(self, request):
        # Get datas and store
        email = request.data.get('customer_email')
        first_name = request.data.get('customer_firstname')
        last_name = request.data.get('customer_lastname')
        customer_mobile = request.data.get('customer_mobile')
        learners = request.data.get('learners')
        # Check learner formation
        for learner in learners:
            if 'profile_name' not in learner or 'profile_dob' not in learner:
                return APIHandler.catch('lack of informations', code='001')
        schedule_id = request.data.get('schedule_id')
        auto_create_account = request.data.get('auto_create_account', 0)
        line_id = request.data.get('line_id')
        if not email or not first_name or not last_name or not customer_mobile or not auto_create_account:
            return APIHandler.catch('lack of informations', code='001')
        
        # Register if auto_create == 1
        if auto_create_account == 1 or auto_create_account == '1':
            letters = string.ascii_letters + string.digits
            password = ''.join(random.choice(letters) for i in range(5))
            register_data = {
                'email': email,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
                'mobile': customer_mobile,
                'country': 'Taiwan'
            }
            # Try to register a account and login with token
            try:
                response = CALL_REQUEST('account', 'post', router=f'/customer/', data=register_data, token=account_token)
                content = json.loads(response.content)
                if content['code'] != 'S001011':
                    return APIHandler.catch(data='This email address has been registered. Please check your verification email again to earn eCredits now!', code='032')
                else:
                    # Login and get token, if create success
                    login_data = {
                        'customer_email':email,
                        'customer_password':password,
                        'appId':4,
                        'deviceType':2
                    }
                    login_response = CALL_REQUEST('lej', 'post', router=f'/login', data=login_data)
                    login_content = json.loads(login_response.content)
                    login_code = login_content['code']
                    if login_code != 0:
                        return APIHandler.catch(data="Fail to login", code='033')
                    else:
                        login_content = login_content['data']
                        customer_info = {
                            'token': login_content['token'],
                            'customerId':login_content['customer_id'],
                            'emailActivate':login_content['email_activate']
                        }

                    # If new account, send password
                    mail_data = {
                        'customer_email':email
                    }
                    # print ('response_send_password_mail', content['code'])
                    try:
                        response_send_password_mail = CALL_REQUEST('lej', 'post', router=f'/mail/forgetPassword', data=mail_data)
                    except:
                        pass
            except:
                customer_info = "Error while creating account"
        else:
            customer_info = 'auto_create_account is set as 0'
        # Insert Guest information
        guest_id = SaveGuestInfos(email, first_name, last_name, customer_mobile)
        # print ('guest_id', guest_id)
        if not guest_id:
            return APIHandler.catch('Saving guest info failed', code='009')
        
        temp_id = StoreTempInfo(email, first_name, last_name, customer_mobile, learners, schedule_id, auto_create_account, guest_id, line_id)

        return APIHandler.catch(data={"temp_id":temp_id, "customerInfo":customer_info}, code='002')
        # Return store id


'''Payment gateway below'''
class PayByCounter(APIView):
    def post(self, request):
        temp_id = request.data.get('temp_id')
        counter_result = Update_Counter_Transaction(temp_id)
        
        if counter_result == '004':
            return APIHandler.catch('Missing temp info', code='004')
        elif counter_result == '020':
            return APIHandler.catch('Sending mail failed', code='020')
        else:
            return APIHandler.catch(data={'transaction_no':counter_result}, code='016')

class PayByMail(APIView):
    def get(self, request):
        temp_id = request.GET.get('temp_id')
        guest_email = request.GET.get('guest_email')
        try:
            schedule_id = GetGuestTempInfo(temp_id).schedule_id
        except:
            return APIHandler.catch('Lack of temp info', code='004')
        class_info = GetClassInfo(schedule_id)
        payment_url = public_url + '/payment/url_guest_pay/' + temp_id + '/'
        data = {
            "guest_email": guest_email,
            "customer_name": 'Guest',
            "payment_url": payment_url,
            "class_name": class_info['class_name'],
            "class_option": class_info['option_name'],
            "class_date" : class_info['schedule_name'],
            "class_time" : class_info['schedule_start_time'] + '-' + class_info['schedule_end_time'],
        }
        if not temp_id or not guest_email:
            return APIHandler.catch('Lack of mail information', code='018')
        url = public_url_sendmail + '/sendmail/payment/'
        send_mail = requests.post(url, json=data)
        try:
            send_mail = eval(send_mail.content)
        except:
            return APIHandler.catch(data='Sending mail fail', code='018')

        # Call email api
        # if mail sent
        if not send_mail['code'] == '005000':
            return APIHandler.catch(data=send_mail, code='018')
        else:
            return APIHandler.catch('Sending mail success', code='019')

class GuestPaynow(APIView):
    def post(self, request):
        # Get datas and check exist
        temp_id = request.data.get('temp_id')
        if not temp_id:
            return APIHandler.catch('Please provide temp_id', code='003')
        temp_info = GetGuestTempInfo(temp_id)
        if not temp_info:
            return APIHandler.catch('Missing temp info', code='004')
        email = temp_info.email
        first_name = temp_info.first_name
        last_name = temp_info.last_name
        customer_mobile = temp_info.mobile
        learners = eval(temp_info.learners)
        schedule_id = temp_info.schedule_id
        # ECPAY_token = request.data.get('ECPAY_token')
        # coupon = request.data.get('coupon')
        auto_create_account = temp_info.auto_create_account
        if not email or not first_name or not last_name or not customer_mobile:
            return APIHandler.catch('Temp info not complete', code='005')

        # Get all needed class info by schedule_id
        class_info = GetClassInfo(schedule_id)
        if not class_info:
            return APIHandler.catch('Schedule not exist', code='006')
        # Confirm that learners and vacancy
        learner_count = len(learners)
        if not learners:
            return APIHandler.catch('Missing learner info', code='007')
        elif learner_count > class_info['vacancy']:
            return APIHandler.catch('No vacancy', code='008')

        guest_id = temp_info.guest_id
        
        # Handle the free class by skip ECPAY
        if class_info['option_price'] <= 0:
            trans = Update_Free_Transaction(temp_id, schedule_id, learners)
            if trans == '006':
                return APIHandler.catch('Schedule not exist', code='006')
            elif trans == '013':
                return APIHandler.catch('Learner dob format not legible', code='013')
            elif trans == '014':
                # print ('trans', trans)
                return APIHandler.catch('Success, free class, go to transactions', code='010')
            elif trans == '020':
                return APIHandler.catch('Sending mail failed', code='020')
            else:
                return APIHandler.catch('Free transaction problem', code='017')

        # Start to ECpay and redirect to payment html 
        # html = ECPAY(schedule_id, learners, guest_id, temp_id)
        pay_data = NEWEBPAY(schedule_id, learners, guest_id, temp_id)
        # print (html)
        # if html:
        #     return render(request, 'ECPAY_pay.html', {'html':html})
        if pay_data:
            return render(request, 'NEWEBPAY_pay.html', {'data':pay_data})
        else:
            return APIHandler.catch('Fail to generate payment page', code='011')

class UrlGuestPaynow(APIView):
    def get(self, request, temp_id):
        temp_id = temp_id
        if not temp_id:
            return APIHandler.catch('Please provide temp_id', code='003')
        temp_info = GetGuestTempInfo(temp_id)
        if not temp_info:
            return APIHandler.catch('Missing temp info', code='004')
        email = temp_info.email
        first_name = temp_info.first_name
        last_name = temp_info.last_name
        customer_mobile = temp_info.mobile
        learners = eval(temp_info.learners)
        schedule_id = temp_info.schedule_id
        # ECPAY_token = request.data.get('ECPAY_token')
        # coupon = request.data.get('coupon')
        auto_create_account = temp_info.auto_create_account
        if not email or not first_name or not last_name or not customer_mobile:
            return APIHandler.catch('Temp info not complete', code='005')

        # Get all needed class info by schedule_id
        class_info = GetClassInfo(schedule_id)
        if not class_info:
            return APIHandler.catch('Schedule not exist', code='006')
        # Confirm that learners and vacancy
        learner_count = len(learners)
        if not learners:
            return APIHandler.catch('Missing learner info', code='007')
        elif learner_count > class_info['vacancy']:
            return APIHandler.catch('No vacancy', code='008')

        guest_id = temp_info.guest_id
        
        # Handle the free class by skip ECPAY
        if class_info['option_price'] <= 0:
            trans = Update_Free_Transaction(temp_id, schedule_id, learners)
            if trans == '006':
                return APIHandler.catch('Schedule not exist', code='006')
            elif trans == '013':
                return APIHandler.catch('Learner dob format not legible', code='013')
            elif trans == '014':
                return APIHandler.catch('Success, free class, go to transactions', code='010')
            else:
                return APIHandler.catch('Free transaction problem', code='017')

        # Start to ECpay and redirect to payment html 
        # html = ECPAY(schedule_id, learners, guest_id, temp_id)
        pay_data = NEWEBPAY(schedule_id, learners, guest_id, temp_id)
        # print (html)
        # if html:
        #     return render(request, 'ECPAY_pay.html', {'html':html})
        if pay_data:
            return render(request, 'NEWEBPAY_pay.html', {'data':pay_data})
        else:
            return APIHandler.catch('Fail to generate payment page', code='011')
        return APIHandler.catch('Sending mail success', code='999')

class LEJ2_CustomerPaynow(APIView):
    def post(self, request):
        # Get shopping cart summary
        logger.info ('web here')
        customer_id = request.data.get('customer_id')
        customer_cart_items = GET_CUSTOMER_CART_ITEMS(customer_id)
        if customer_cart_items.count == 0:
            return APIHandler.catch('No class in customer\'s cart', code='024')

        cart_price = 0
        for shopping_cart_info in customer_cart_items:
            # shoppingcart_id = cart_item.shoppingcart_id
            # shopping_cart_info = GET_SHOPPINGCART_INFOS(shoppingcart_id)
        # if shopping_cart_info == '022':
        #     return APIHandler.catch('Missing shopping cart informations', code='022')
        # elif not shopping_cart_info:
        #     return APIHandler.catch('Missing temp info', code='004')
        # logger.info (f'cart info here {shopping_cart_info}')
        # auto_create_account = temp_info.auto_create_account
        # THIS ONE IS FOR GUESTPAY on WEB

            # Get all needed class info by schedule_id
            shoppingcart_id = shopping_cart_info.id
            cart_infos = GET_SHOPPINGCART_INFOS(shoppingcart_id)
            schedule_id = cart_infos['schedule_id']
            learners = cart_infos['learners']
            class_info = GetClassInfo(schedule_id)
            if not class_info:
                return APIHandler.catch('Schedule not exist', code='006')
            # Confirm vacancy
            learner_count = len(learners)
            if not learners:
                return APIHandler.catch('Missing learner info', code='007')
            elif learner_count > class_info['vacancy']:
                return APIHandler.catch('No vacancy', code='008')
            cart_price += class_info['option_price']
        
        # Handle the free class by skip ECPAY
        if cart_price <= 0:
            trans = Update_Free_LEJ2_Transaction(customer_id)
            if trans == '006':
                return APIHandler.catch('Schedule not exist', code='006')
            elif trans == '013':
                return APIHandler.catch('Learner dob format not legible', code='013')
            elif trans == '014':
                return APIHandler.catch('Success, free class, go to transactions', code='010')
            else:
                return APIHandler.catch('Free transaction problem', code='017')

        # Start to ECpay and redirect to payment html 
        # html = ECPAY(schedule_id, learners, guest_id, temp_id)
        pay_data = LEJ2_NEWEBPAY(customer_id)
        # print (html)
        # if html:
        #     return render(request, 'ECPAY_pay.html', {'html':html})
        if pay_data:
            return render(request, 'NEWEBPAY_pay.html', {'data':pay_data})
        else:
            return APIHandler.catch('Fail to generate payment page', code='011')
        return APIHandler.catch('Sending mail success', code='999')

class LEJ2_Url_CustomerPaynow(APIView):
    def get(self, request, customer_id):
        customer_id = customer_id
        if not customer_id:
            return APIHandler.catch('Please provide customer_id', code='003')
        customer_cart_items = GET_CUSTOMER_CART_ITEMS(customer_id)
        # print('customer_cart_sum', customer_cart_sum)
        if customer_cart_items.count == 0:
            return APIHandler.catch('No class in customer\'s cart', code='024')

        cart_price = 0
        for shopping_cart_info in customer_cart_items:

            # Get all needed class info by schedule_id
            shoppingcart_id = shopping_cart_info.id
            cart_infos = GET_SHOPPINGCART_INFOS(shoppingcart_id)
            schedule_id = cart_infos['schedule_id']
            learners = cart_infos['learners']
            class_info = GetClassInfo(schedule_id)
            if not class_info:
                return APIHandler.catch('Schedule not exist', code='006')
            # Confirm vacancy
            learner_count = len(learners)
            if not learners:
                return APIHandler.catch('Missing learner info', code='007')
            elif learner_count > class_info['vacancy']:
                return APIHandler.catch('No vacancy', code='008')
            cart_price += class_info['option_price']
        
        # Handle the free class by skip ECPAY
        if cart_price <= 0:
            trans = Update_Free_LEJ2_Transaction(customer_id)
            if trans == '006':
                return APIHandler.catch('Schedule not exist', code='006')
            elif trans == '013':
                return APIHandler.catch('Learner dob format not legible', code='013')
            elif trans == '014':
                return APIHandler.catch('Success, free class, go to transactions', code='010')
            else:
                return APIHandler.catch('Free transaction problem', code='017')

        # Start to ECpay and redirect to payment html 
        # html = ECPAY(schedule_id, learners, guest_id, temp_id)
        pay_data = LEJ2_NEWEBPAY(customer_id)
        # print (html)
        # if html:
        #     return render(request, 'ECPAY_pay.html', {'html':html})
        if pay_data:
            return render(request, 'NEWEBPAY_pay.html', {'data':pay_data})
        else:
            return APIHandler.catch('Fail to generate payment page', code='011')
        return APIHandler.catch('Sending mail success', code='999')

class Url_PremiumCustomerPaynow(APIView):
    def get(self, request, service_customer_id, contract_type='Annual'):
        # Redirect to newebpay page
        if contract_type == 'Annual' or not contract_type:
            premium_price = 1000
            merchant_order_no = STORE_SHOPPINGCART_PREMIUM(service_customer_id, premium_price)
            if not merchant_order_no:
                return APIHandler.catch('Fail to store premiun to cart', code='031')
            pay_data = PREMIUM_NEWEBPAY(merchant_order_no, contract_type)
            if pay_data:
                return render(request, 'NEWEBPAY_pay.html', {'data':pay_data})
            else:
                return APIHandler.catch('Fail to generate payment page', code='011')

        elif contract_type == 'Monthly':
            premium_price = 99
            merchant_order_no = STORE_SHOPPINGCART_PREMIUM(service_customer_id, premium_price)
            if not merchant_order_no:
                return APIHandler.catch('Fail to store premiun to cart', code='031')
            pay_data = PREMIUM_NEWEBPAY(merchant_order_no, contract_type)
            if pay_data:
                return render(request, 'NEWEBPAY1.1_pay.html', {'data':pay_data})
            else:
                return APIHandler.catch('Fail to generate payment page', code='011')
        else:
            return APIHandler.catch('Contract type not correct', code='034')
        
class Token_Charge(APIView):    
    def post(self, request):
        service_customer_id = request.data.get('service_customer_id')
        token = GET_AUTHORIZED_TOKEN(service_customer_id)
        premium_price = 99
        if not token:
            logger.error(f'Get authorized token failed, service_customer_id {service_customer_id}')
            return APIHandler.catch('This customer has no charge token', code='037')
        merchant_order_no = STORE_SHOPPINGCART_PREMIUM(service_customer_id, premium_price)
        if not merchant_order_no:
            return APIHandler.catch('Fail to store premiun to cart', code='031')
        result = CHARGEBYTOKEN_NEWEBPAY(merchant_order_no, token)
        if result['Status'] == 'SUCCESS':
            data = result['Result']
            transaction_id = UPDATE_PREMIUM_TRANSACTION(merchant_order_no, data)
            return APIHandler.catch({'transaction_id':transaction_id}, code='036')
        else:
            logger.error(f'Fail to charge with token, service_customer_id {service_customer_id}')
            return APIHandler.catch('Fail to charge with token', code='000')

class Url_FastLaunch_Paynow(APIView):
    def get(self, request, charge_type, fastlaunch_no, email):
        pay_data = FASTLAUNCH_NEWEBPAY(fastlaunch_no, email,charge_type)

        if pay_data:
            return render(request, 'NEWEBPAY_pay.html', {'data':pay_data})
        else:
            return APIHandler.catch('fail', code='000')


'''ReturnData below''' 
class NEWEBPAY_ReturnData(APIView):
    def post(self, request):
        # Get transaction data
        data = request.data
        # print ('newebpay_data', data)
        decrypt_data = NEWEBPAY_Decrypt(data['TradeInfo'])
        temp_id = decrypt_data['Result']['MerchantOrderNo']
        temp_info = GetGuestTempInfo(temp_id)
        schedule_id = temp_info.schedule_id

        if data['Status'] != 'SUCCESS':
            logger.error (f'Fail to charge with credit card, transaction number(temp_id) {temp_id}')
            return APIHandler.catch('Fail to charge', code='999')

        if not temp_info:
            return APIHandler.catch('Missing temp info', code='004')
        learners = eval(temp_info.learners)
        # Get all needed class info by schedule_id
        class_info = GetClassInfo(schedule_id)

        

        # Get credict_return_data
        credict_return_data = 'NEWEBPAY'
        # Todo here: check credict card record in newebpay
        
        # Start transaction to transactions
        trans = Update_Transaction(temp_id, schedule_id, learners, class_info, credict_return_data, newebpay_decrypt_data=decrypt_data['Result'])
        if trans == '006':
            return APIHandler.catch('Schedule not exist', code='006')
        elif trans == '013':
            return APIHandler.catch('Learner dob format not legible', code='013')
        
        else:
            print ('trans', trans)
            return APIHandler.catch('ok', code='014')

class NEWEBPAY_LEJ2_ReturnData(APIView):
    def post(self, request):
        # Get transaction data
        data = request.data
        # print ('newebpay_data', data)
        decrypt_data = NEWEBPAY_Decrypt(data['TradeInfo'])
        # print ('dec newebpay_data', decrypt_data)
        shoppingcart_summary_id = decrypt_data['Result']['MerchantOrderNo']
        customer_id = GET_CUSTOMERID_BY_SUMID(shoppingcart_summary_id)
        if not customer_id:
            return APIHandler.catch('Missing shopping cart informations', code='022')
        # print ('shoppingcart_id', customer_id)
        if data['Status'] != 'SUCCESS':
            logger.error (f'Fail to charge with credit card, transaction number(customer_id) {customer_id}')
            return APIHandler.catch('Newebpay Fail to charge', code='023')

        # Get credict_return_data
        credict_return_data = 'NEWEBPAY'
        # Todo here: check credict card record in newebpay
        
        # Start transaction to transactions
        trans = Update_LEJ2_Transaction(customer_id, credict_return_data, newebpay_decrypt_data=decrypt_data['Result'])
        if trans == '006':
            return APIHandler.catch('Schedule not exist', code='006')
        elif trans == '013':
            return APIHandler.catch('Learner dob format not legible', code='013')
        
        else:
            # print ('trans', trans)
            return APIHandler.catch('ok', code='014')

class NEWEBPAY_Premium_ReturnData(APIView):
    def post(self, request):
        # Get transaction data
        data = request.data
        decrypt_data = NEWEBPAY_Decrypt(data['TradeInfo'])
        merchant_order_no = decrypt_data['Result']['MerchantOrderNo']
        service_customer_id = GET_PREMIUM_INFO(merchant_order_no).service_customer_id
        if not service_customer_id:
            return APIHandler.catch('Missing premium informations', code='030')
        if data['Status'] != 'SUCCESS':
            logger.error (f'Fail to charge with credit card, transaction number(customer_id) {customer_id}')
            return APIHandler.catch('Newebpay Fail to charge', code='023')
        
        # Update transaciton
        transaction_id = UPDATE_PREMIUM_TRANSACTION(merchant_order_no, decrypt_data['Result'])

        # Upate premium privilege via account service
        # 1 YEAR for this return data
        plus_date = 365
        update_period_data = CALCULATE_PREMIUM_VALID_PERIOD(service_customer_id, plus_date)
        update_period_data['transaction_id'] = transaction_id
        response = CALL_REQUEST('account', 'post', router=f'/customer/{service_customer_id}/plan/', data=update_period_data, token=account_token)
        update_result = json.loads(response.content)
        if not response:
            logger.error(f'Account service no response while updating premium, service_customer_id {service_customer_id}')
        elif update_result['code'] != 'S001018':
            logger.error(f'Account service failed while updating premium, service_customer_id {service_customer_id}')
            
        return APIHandler.catch('Success', code='000')

class NEWEBPAY_PremiumAuthorized_ReturnData(APIView):
    def post(self, request):
        # Get transaction data
        data = request.data
        data = json.loads(data['JSONData'])
        print ('DATA will be used for token storage', data)
        decrypt_data = json.loads(data['Result'])
        merchant_order_no = decrypt_data['MerchantOrderNo']

        premium_cart_info = GET_PREMIUM_INFO(merchant_order_no)
        lej_customer_id = premium_cart_info.lej_customer_id
        service_customer_id = GET_PREMIUM_INFO(merchant_order_no).service_customer_id
        if not service_customer_id:
            return APIHandler.catch('Missing premium informations', code='030')
        if data['Status'] != 'SUCCESS':
            logger.error (f'Fail to charge with credit card, transaction number(customer_id) {customer_id}')
            return APIHandler.catch('Newebpay Fail to charge', code='023')
        
        # Save token for future charge
        authorized_token = decrypt_data['TokenValue']
        toekn_life = decrypt_data['TokenLife']
        save_toekn = SAVE_AUTHORIZED_TOKEN(authorized_token, toekn_life, lej_customer_id, service_customer_id)
        if not save_toekn:
            logger.error(f'Save authorized token failed, service_customer_id {service_customer_id}')
            return APIHandler.catch('Save authorized token failed', code='000')

        # Update transaciton
        transaction_id = UPDATE_PREMIUM_TRANSACTION(merchant_order_no, decrypt_data)

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
        
        return APIHandler.catch('Success', code='000')

class NEWEBPAY_Fastlaunch_ReturnData(APIView):
    def post(self, request):
        # Get transaction data
        data = request.data
        decrypt_data = NEWEBPAY_Decrypt(data['TradeInfo'])
        newebpay_decrypt_data = decrypt_data['Result']
        trans = UPDATE_FASTLAUNCH_TRANSACTION(newebpay_decrypt_data)
        if trans:
            return APIHandler.catch({'transaction success': trans}, code='014')
        else:
            return APIHandler.catch('fail', code='000')


class ECPAY_ReturnData(APIView):
    def post(self, request):
        data = request.data
        MerchantTradeNo = data['MerchantTradeNo']
        trade = ECPAY_TradeInfo(MerchantTradeNo)

        # Get payment informations
        credict_return_data = trade
        schedule_id = eval(data['CustomField1'])['s_id']
        temp_id = eval(data['CustomField3'])['t_id']
        temp_info = GetGuestTempInfo(temp_id)
        if not temp_info:
            return APIHandler.catch('Missing temp info', code='004')
        learners = eval(temp_info.learners)
        # Get all needed class info by schedule_id
        class_info = GetClassInfo(schedule_id)
        
        # Start transaction to transactions
        trans = Update_Transaction(temp_id, schedule_id, learners, class_info, credict_return_data)
        if trans == '006':
            return APIHandler.catch('Schedule not exist', code='006')
        elif trans == '013':
            return APIHandler.catch('Learner dob format not legible', code='013')
        elif trans == '020':
            return APIHandler.catch('Sending mail failed', code='020')
        else:
            # print ('trans', trans)
            return APIHandler.catch('ok', code='014')


'''Open for front-end to use'''
class HistoryLearners(APIView):
    def get(self, request):
        # Use get method with parameters?=
        email = request.GET.get('guest_email')
        # print ('email:', email)
        learners = GetHistroyLearners(email)

        return APIHandler.catch(data=learners, code='015')

class GetTransactionNo(APIView):
    def get(self, request):
        temp_id = request.GET.get('temp_id')
        if not temp_id:
            return APIHandler.catch('Please provide temp_id', code='003')
        trans_no = GetTransactionNumber(temp_id)
        trans_id = GetTransactionID(temp_id)
        if not trans_no:
            return APIHandler.catch('Transaction not found', code='021')
        else:
            return APIHandler.catch(data={'transaction_no':trans_no, 'transaction_id':trans_id}, code='000')

class LinePaymentHistory(APIView):
    def get(self, request):
        # Use line id to search for history transactions
        line_id = request.GET.get('line_id')
        trans_items = GetLineTransactions(line_id)
        if not trans_items:
            return APIHandler.catch('Transaction not found', code='021')
        else:
            return APIHandler.catch(data=trans_items, code='000')

class LEJ2_CleanUpShoppingCart(APIView):
    def delete(self, request):
        # Use customer_id to clean all classes in shopping cart
        customer_id = request.data.get('customer_id')
        if not customer_id:
            return APIHandler.catch('Need customer_id', code='025')
        clear_state = CLEAN_SHOPPINGCART(customer_id)
        if not clear_state:
            return APIHandler.catch('Customer not exist', code='026')
        return APIHandler.catch('Shopping cart clear', code='027')

class LEJ2_GetShoppingcart_Summary_ID(APIView):
    def get(self, request):
        customer_id = request.GET.get('customer_id')
        if not customer_id:
            return APIHandler.catch('Need customer_id', code='025')
        summary_id = GET_SHOPPINGCART_SUM_ID(customer_id)
        if not summary_id:
            return APIHandler.catch('Shopping car no summary yet', code='028')
        else:
            return APIHandler.catch(data={'summary_id':summary_id}, code='000')

class Newebpay_Trade_Info(APIView):
    def get(self, request, newebpay_merchant_trade_no):
        
        trade_info = GET_TRADE_INFO(newebpay_merchant_trade_no)
        
        return APIHandler.catch(data={'trade_info':trade_info}, code='099')


'''Test below'''
class ClosePage(APIView):
    def get(self, request):
        return render(request, 'close_page.html')

class Result(APIView):
    def get(self, request, newebpay_merchant_trade_no):

        CHARGEBYTOKEN_NEWEBPAY(merchant_order_no, token)
        trade_info = GET_TRADE_INFO(newebpay_merchant_trade_no)
        
        # print ('OOOOOOOOOOOOo', update_result)
        
        
        # CREATE_MULTITRANSACTION()
        return APIHandler.catch('Missing shopping cart informations', code='022')



# class Url_TokenCharge_paynow(APIView):
    