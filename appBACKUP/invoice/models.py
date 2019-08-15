from django.db import models
from django.utils import timezone

# Create your models here.

class InvoiceHistory(models.Model):
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    invoice_number = models.CharField(max_length=255, blank=True, null=True)
    merchant_order_number = models.CharField(max_length=255, blank=True, null=True)
    total_amt = models.IntegerField(blank=True, null=True)
    invoice_status = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.created_at = timezone.now()
        super(InvoiceHistory, self).save(*args, **kwargs)


    class Meta:
        managed = True
        db_table = 'invoice_history'
'''
{'Status': 'SUCCESS', 'Message': '發票開立成功', 
'Result': '{"CheckCode":"5A8E0E504C1F12C3B3AA8377C841A577D22AEDC73550DA32F13F87FAB5A25753",
"MerchantID":"31601777",
"MerchantOrderNo":"nm2v5kkjzx1hkq0anrda",
"InvoiceNumber":"AE10203008",
"TotalAmt":55660,
"InvoiceTransNo":"19070310355060573",
"RandomNum":"2454",
"CreateTime":"2019-07-03 10:35:50",
"BarCode":"10808AE102030082454",
"QRcodeL":"AE10203008108070324540000ce8d0000d96c0000000082862223JCRbFmyg9bTVTASfM\\/e3tw==:**********:1:1:1:\\u8ab2\\u7a0b:1:55660","QRcodeR":"**"}
'''