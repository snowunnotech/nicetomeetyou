from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('b2c_invoice/', views.CreateB2CInvoice.as_view()),
    # path('guest_tempinfo/', views.StoreGuestTempInfo.as_view()),
    # url(r'^url_guest_pay/(?P<temp_id>[\w\x2D]+)/$', views.MailGuestPaynow.as_view()),
]