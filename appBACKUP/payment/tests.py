from django.test import TestCase

# Create your tests here.
from .services import *


class Test1(TestCase):
    def __init__(self):
        self.credict_return_data = {'ATMAccBank': '', 'ATMAccNo': '',  'AlipayID': '', 'AlipayTradeNo': '', 'CustomField1': {'schedule_id': 'zpeexbynq0lazeymm4rs'}, 'CustomField2': '', 'CustomField3': '', 'CustomField4': '', 'ExecTimes': '', \
        'Frequency': '', 'HandlingCharge': '55', 'ItemName': [{'profile_name': 'Candy Yo', 'profile_dob': '2016/3/28', 'profile_note': ''}, {'profile_name': 'Candys Yo', \
        'profile_dob': '2016/3/28', 'profile_note': 'cc'}],'MerchantID': '2000214', 'MerchantTradeNo': 'NO20190508043305', 'PayFrom': '', 'PaymentDate': '2019/05/08 12:33:27', \
        'PaymentNo': '', 'PaymentType': 'Credit_CreditCard', 'PaymentTypeChargeFee': '55', 'PeriodAmount': '', 'PeriodType': '', 'StoreID': '',  'TenpayTradeNo': '', \
        'TotalSuccessAmount': '', 'TotalSuccessTimes': '', 'TradeAmt': '2000', 'TradeDate': '2019/05/08 12:33:05', 'TradeNo': '1905081233057184', 'TradeStatus': '1', 'WebATMAccBank': '', \
        'WebATMAccNo': '', 'WebATMBankName': '', 'amount': '2000', 'auth_code': '777777',  'card4no': '2222', 'card6no': '431195', \
        'eci': '0', 'gwsr': '10853033', 'process_date': '2019/05/08 12:33:27', 'red_dan': '0', 'red_de_amt': '0', 'red_ok_amt': '0', 'red_yet': '0', \
        'staed': '0', 'stage': '0', 'stast': '0'}
        print ('SSSSSSSSSs')
    def setUp(self):
        print ('credict_return_data')
        print ('credict_return_data', self.credict_return_data)

if __name__ == '__main__':
    process = Test1()
    process.setUp()



