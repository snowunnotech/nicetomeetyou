from helper.helper import APIHandler
from django.db import transaction
from decimal import Decimal, ROUND_HALF_UP
import time, os, json
from payment.gateway_service import *
import requests

INVOICE_URL = os.getenv('INVOICE_URL')
INVOICE_MERCHANT_ID = os.getenv('INVOICE_MERCHANT_ID')
INVOICE_KEY = os.getenv('INVOICE_KEY')
INVOICE_IV = os.getenv('INVOICE_IV')

def CREATE_B2C_CREDITCARD_INVOICE(data):
    # Accept invoice data
    # data = {
    #     'ItemCount':[]
    #     'ItemPrice':[]
    #     'MerchantOrderNo':str
    #     'BuyerName':str
    #     'BuyerEmail':str
    #     'ItemName':[]
    #     'ItemUnit':str
    #     'Card4No':[]
    # }
    try:
        MerchantOrderNo = data['MerchantOrderNo']
        Card4No = '信用卡末四碼: ' + data['Card4No']
        BuyerEmail = data['BuyerEmail']
        BuyerName = data['BuyerName']
        ItemUnit = data['ItemUnit']
        ItemName = data['ItemName']
        item_count = data['ItemCount']
        item_price = data['ItemPrice']
    except:
        return 'Lack of data'
    
    # # Calculation of tax (每個課程都顯示的狀況，目前不採用)
    # item_len = len(item_counts)
    # for i in range(item_len):
    #     item_count = item_counts[i]
    #     item_price = item_prices[i]
    #     origin_item_amt_list = []
    #     tax_amt_list = []
    #     amt_list = []
    #     total_amt_list = []

    #     origin_item_amt = int(item_count * item_price)
    #     tax_amt_raw = origin_item_amt*0.05
    #     tax_amt = int(Decimal(f'{tax_amt_raw}').quantize(Decimal('1.'), rounding=ROUND_HALF_UP))
    #     amt = origin_item_amt - tax_amt
    #     total_amt = amt + tax_amt

    #     origin_item_amt_list.append(origin_item_amt)
    #     tax_amt_list.append(tax_amt)
    #     amt_list.append(amt)
    #     total_amt_list.append(total_amt)

    # item_count = '|'.join(item_counts)
    # item_price = '|'.join(item_prices)
    # origin_item_amt = '|'.join(origin_item_amt_list)
    # tax_amt = '|'.join(tax_amt_list)
    # amt = '|'.join(amt_list)
    # total_amt = '|'.join(total_amt_list)
    origin_item_amt = int(item_count * item_price)
    tax_amt_raw = origin_item_amt*0.05
    tax_amt = int(Decimal(f'{tax_amt_raw}').quantize(Decimal('1.'), rounding=ROUND_HALF_UP))
    amt = origin_item_amt - tax_amt
    total_amt = amt + tax_amt
    
    order_params={
        'RespondType': 'JSON',
        'Version': '1.4',
        'TimeStamp': f'{int(time.time())}',
        'MerchantOrderNo': MerchantOrderNo,
        'Status': '1', # 1=即時開立
        # 'CreateStatusTime' 預設開立日期
        'Category': 'B2C',  # B2B or B2C
        'BuyerName': BuyerName,  # Customer name
        # 'BuyerAddress': data['customer_address']
        'BuyerEmail': BuyerEmail,  # Customer email
        'PrintFlag': 'Y', # Y=索取發票
        'ItemName': ItemName, # 單項：商品一  多項：商品一｜商品二｜...
        'ItemCount': item_count, # 商品數量，多項模式同itemname
        'ItemUnit': ItemUnit, #商品單位
        'ItemPrice': item_price, #商品單價
        'ItemAmt': origin_item_amt,#數量*單價
        'TaxType':'1', # 1=應稅
        'TaxRate':5, # 5為一般稅率
        'Amt': int(amt),# 銷售金額
        'TaxAmt': int(tax_amt), # 銷售金額的5%
        'TotalAmt': int(total_amt), # Amt + TaxAmt
        'Comment': Card4No#信用卡末四碼：1234
    }
    print ('order_params ', order_params)

    # AES encode
    key = INVOICE_KEY
    iv = INVOICE_IV
    AES_info_str = NEWEBPAY_AES(order_params, key, iv)

    # Call invoice api
    url = INVOICE_URL
    post_data = {
        'MerchantID_': INVOICE_MERCHANT_ID,
        'PostData_': AES_info_str
    }
    try:
        response = requests.post(url=url, data=post_data)
    except:
        response = None
    return response
