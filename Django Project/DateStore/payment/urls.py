from django.urls import path
from payment.views import *
urlpatterns = [
    path('payment_success',payment_success,name='payment_success'),
    path('checkout',checkout,name='checkout'),
    path('billing_info',billing_info,name='billing_info'),
]

