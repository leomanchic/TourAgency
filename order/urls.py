from django.urls import path
from .views import start_order, pay_err

urlpatterns = [
    path("start_order/", start_order, name='start_order'),
    path("pay_error/",pay_err, name='pay_err')
]
