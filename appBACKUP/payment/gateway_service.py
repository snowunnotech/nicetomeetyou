from django.apps import apps
from Crypto.Cipher import AES
import urllib.parse
import binascii
import hashlib
import json, string, uuid, os, time, requests


'''Encrypt/Decrypt'''

def AES_encrypt(data, key, iv):
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    return cryptor.encrypt(data)

def AES_decrypt(data, key, iv):
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    return cryptor.decrypt(data)

def NEWEBPAY_AES(order_params, key, iv):
    # parameter to url query string
    order_params = urllib.parse.urlencode(order_params)
    # print ('order_params', order_params)
    # parameter padding, AES256 encode
    BS = 32
    pad_params = order_params + (BS - len(order_params) % BS) * chr(BS - len(order_params) % BS)
    AES_info = AES_encrypt(pad_params, key, iv)
    # print ('AES_info', AES_info)
    AES_info_str = str(binascii.hexlify(AES_info), 'ascii')
    # print ('AES_info_str', AES_info_str)
    return AES_info_str

def NEWEBPAY_SHA(AES_plus):
    m = hashlib.sha256()
    m.update(AES_plus.encode('ascii'))
    SHA_info = m.digest()
    SHA_info_str = str(binascii.hexlify(SHA_info), 'ascii')
    SHA_info_STR = SHA_info_str.upper()
    # print ('SHA_info_STR', SHA_info_STR)
    return SHA_info_STR
    
def NEWEBPAY_AES_decrypt(AES_info_str, key, iv):
    # print ('AES_info_str', AES_info_str)
    AES_info = AES_info_str.encode('utf-8')
    # print ('AES_info_str22utf-8', AES_info)
    AES_info = binascii.unhexlify(AES_info)
    # print ('AES_info_unhexlify', AES_info)
    AES_info = AES_decrypt(AES_info, key, iv)
    # print ('raw decrypt AES_info', AES_info)
    # AES_info = str(AES_info, 'ascii')
    AES_info = AES_info.decode("utf-8")
    padding_str = AES_info[-1]
    # print ('padding_str', padding_str)
    AES_info = AES_info.strip(padding_str)
    # print ('AES_info', AES_info)
    AES_info = json.loads(AES_info)
    # print ('AES_info2', AES_info)
    return (AES_info)

def UNIQUE_ID_GENERATOR(object, number=30):
    ID = str(uuid.uuid4())[0:number]
    try:
        trans_count = object.objects.filter(id=ID).count()
        while trans_count>0:
            ID = str(uuid.uuid4())[0:number]
            trans_count = object.objects.filter(id=ID).count()
    except:
        pass
    return ID


'''Check out transactions'''

def GET_TRADE_INFO(newebpay_merchant_trade_no):

    Transaction = apps.get_model('payment', 'Transaction')
    txn_info = Transaction.objects.get(newebpay_merchant_trade_no=newebpay_merchant_trade_no)
    
    # Collect information
    MerchantID = os.getenv('MERCHANT_ID')
    key = os.getenv('NEWEBPAY_KEY')
    iv = os.getenv('NEWEBPAY_IV')
    Version = 1.1
    RespondType = 'JSON'
    TimeStamp = f'{int(time.time())}'
    MerchantOrderNo = newebpay_merchant_trade_no
    Amt = int(txn_info.total_price)

    order_params = {
        'MerchantID':MerchantID,
        'Version':Version,
        'RespondType':RespondType,
        'TimeStamp':TimeStamp,
        'MerchantOrderNo':MerchantOrderNo,
        'Amt':Amt,
    }

    # Fit in checkvalue
    CheckValue =''
    checkitems = ['Amt','MerchantID','MerchantOrderNo']
    for item in checkitems:
        CheckValue+=f'{item}={order_params[item]}&'
    CheckValue = CheckValue[0:-1]
    CheckValue = 'IV=' + iv + '&' + CheckValue + '&' + 'Key=' + key
    CheckValue = NEWEBPAY_SHA(CheckValue)
    order_params['CheckValue'] = CheckValue

    # Request
    url = os.getenv('NEWEBPAY_TRADE_INFO_URL')
    response = requests.post(url, data=order_params)
    info = json.loads(response.content)['Result']

    return info