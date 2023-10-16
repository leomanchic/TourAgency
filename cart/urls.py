from django.urls import path
from cart.views import cart, add_to_cart, checkout

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

    path("", cart, name='cart'),
    path("checkout", checkout, name='checkout'),

]
