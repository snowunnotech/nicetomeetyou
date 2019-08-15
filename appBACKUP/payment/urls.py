from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('hello_world/', views.Hello.as_view()),
    path('guest_tempinfo/', views.StoreGuestTempInfo.as_view()),
    path('newebpay_guest_paynow/', views.GuestPaynow.as_view()),
    path('lej2_customer_paynow/', views.LEJ2_CustomerPaynow.as_view()),
    # Return data url
    path('ecpay_return_data/', views.ECPAY_ReturnData.as_view()),
    path('newebpay_return_data/', views.NEWEBPAY_ReturnData.as_view()),
    path('newebpay_return_lej2_data/', views.NEWEBPAY_LEJ2_ReturnData.as_view()),
    path('newebpay_return_premium_data/', views.NEWEBPAY_Premium_ReturnData.as_view()),
    path('newebpay_return_premiumauthorized_data/', views.NEWEBPAY_PremiumAuthorized_ReturnData.as_view()),
    path('newebpay_return_fastlaunch_data/', views.NEWEBPAY_Fastlaunch_ReturnData.as_view()),
    # payment
    path('pay_by_counter/', views.PayByCounter.as_view()),
    path('pay_by_mail/', views.PayByMail.as_view()),
    url(r'^url_guest_pay/(?P<temp_id>[\w\x2D_]+)/$', views.UrlGuestPaynow.as_view()),
    url(r'^lej2_url_customer_pay/(?P<customer_id>[\w\x2D_]+)/$', views.LEJ2_Url_CustomerPaynow.as_view()),
    url(r'^fastlaunch_url_pay/(?P<charge_type>[\w]+)/(?P<fastlaunch_no>[\w\x2D_]+)/(?P<email>[\w\x2D\@\.]+)/$', views.Url_FastLaunch_Paynow.as_view()),
    url(r'^premium_url_pay/(?P<service_customer_id>[\w\x2D_]+)/$', views.Url_PremiumCustomerPaynow.as_view()),
    url(r'^premium_url_pay/(?P<service_customer_id>[\w\x2D_]+)/(?P<contract_type>[\w\x2D]+)/$', views.Url_PremiumCustomerPaynow.as_view()),
    # Test
    path('close_page/', views.ClosePage.as_view()),
    path('show_result/', views.Result.as_view()),
    url(r'^show_result/(?P<newebpay_merchant_trade_no>[\w\x2D_]+)/$', views.Result.as_view()),
    # Other api for front-end
    path('history_learners/', views.HistoryLearners.as_view()),
    path('transaction_no/', views.GetTransactionNo.as_view()),
    path('line_payment_history/', views.LinePaymentHistory.as_view()),
    path('lej2_clean_shoppingcart/', views.LEJ2_CleanUpShoppingCart.as_view()),
    path('lej2_shoppingcart_sumID/', views.LEJ2_GetShoppingcart_Summary_ID.as_view()),
    url(r'^newebpay_trade_info/(?P<newebpay_merchant_trade_no>[\w\x2D_]+)/$', views.Newebpay_Trade_Info.as_view()),
    # Not yet on api gateway
    path('token_charge/', views.Token_Charge.as_view()),
    # Not yet swagger
]