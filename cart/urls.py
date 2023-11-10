from django.urls import path
from cart.views import cart, add_to_cart, checkout, hx_menu_cart, hx_cart_total, update_cart, payout, success_pay

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

    path("", cart, name='cart'),
    path("checkout/", checkout, name='checkout'),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
    path('hx_cart_total/', hx_cart_total, name='hx_cart_total'),
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
    path('payout/', payout, name='payout'),
    path('success/', success_pay, name='success_pay')

]
