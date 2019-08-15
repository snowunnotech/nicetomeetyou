import random, string
# from django.conf import settings
from rest_framework.response import Response

# class URL:
#     @staticmethod
#     def url_ba():
#         url = settings.BA_URL_TEST if settings.DEBUG else settings.BA_URL_RELEASE
#         return url+settings.BA_API_PRIFIX

class APIHandler:
    @staticmethod
    def success(data, code):
        return Response({'code': '003'+code, 'data': data})
    
    @staticmethod
    def catch(data, code):
        return Response({'code': 'S003'+code, 'data': data})

    @staticmethod
    def fail(msg, code=99):
        return Response({'code': code, 'msg': msg})

class Message():
    #default
    noAuth = 'You have been log out'
    # unknown = 'Unknown'
    # un_find = 'No data found'
    # request_error = 'Request error'
    # account_already_exist = 'This account has already been registered.'
    # already_exist = 'Already exist'
    # # do_nothing = 'Do nothing'
    # success = 'Success'

    # #others 
    # teacher_id_empty = 'Teacher Id is required'
    # customer_id_empty = 'Customer Id is required'
    # vendor_id_empty = 'Vendor Id is required'
    # type_id_empty = 'Type Id is required'

    # email_empty = 'Email is required'
    # password_empty = 'Password is required'
    # last_name_empty = 'Last name is required'
    # first_name_empty = 'First name is required'
    # token_empty = 'Token is required'

    # old_password_empty = 'Old password is required'
    # old_password_is_not_corrent = 'Old password is not correct'

    # invalid_customer = 'The customer is invalid'
    # invalid_header = 'Invalid header found'
    # invalid_teacher = "The teacher is invalid"
    # invalid_group = "The group is invalid"
    # invalid_email_or_password = 'Invalid email or password'
    # invalid_invite_type = 'The invite type is invalid'

    # error_when_get_token = 'Error occurred when getting token'
    # error_when_get_customer = 'Error occurred when retrieving customer information'
    # error_token = 'Error occurred when validating token'

    # emial_already_exist = 'Email already exists'
    # exceed_tag_maximum = "Maximum two tags are allowed"
    # only_integer_allow = "Only type integer is allowed"
    # password_not_match = 'Password does not match'
    # create_success_but_invite_error = 'Create account successfully, please check invite'
    # invite_not_find = 'invite not find'

def random_digit_challenge():
    ret = u''
    for i in range(4):
        ret += str(random.randint(0,9))
    return ret, ret
