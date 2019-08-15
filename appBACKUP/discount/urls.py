from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('hello_world/', views.Hello.as_view()),
    # path('guest_tempinfo/', views.StoreGuestTempInfo.as_view()),
    # url(r'^url_guest_pay/(?P<temp_id>[\w\x2D]+)/$', views.UrlGuestPaynow.as_view()),
    path('topex_member/', views.Activate_Topex_Customer.as_view()),
    path('ecredit/', views.Ecredit_Amount.as_view()),
]