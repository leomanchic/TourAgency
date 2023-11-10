import json

import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from order.models import Order
from products.models import Product
# Create your views here.
from .cart import Cart


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/partials/menu_cart.html')


def cart(request):
    return render(request, 'cart/cart.html')


def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'get_thumbnail': product.get_thumbnail(),
                'price': product.price,
            },
            'total_price': (quantity * product.price),
            'quantity': quantity,
        }
    else:
        item = None

    response = render(request, 'cart/partials/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response


@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')


@login_required
def payout(request):
    return render(request, 'cart/partials/payout.html')


def success_pay(request):
    url = 'https://api.oxapay.com/merchants/inquiry'
    track_id = request.GET.get('trackId', None)
    order = Order.objects.get(lid=track_id)

    data = {
        'merchant': settings.OXA_PAY_KEY,
        'trackId': track_id
    }
    response = requests.post(url, data=json.dumps(data))
    result = response.json()
    # print(result)

    # проверка статуса оплаты
    if result['status'] == 'Paid':
        order.paid = True
        order.paid_amount = order.amount_to_pay
        order.save()
    else:
        return redirect(settings.LINK_ERROR_PAY)

    return render(request, 'cart/success.html')


def hx_menu_cart(request):
    return render(request, 'cart/partials/menu_cart.html')


def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')
