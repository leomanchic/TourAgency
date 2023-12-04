import json

from django.conf import settings
from django.shortcuts import render, redirect
import uuid

from django.template.defaulttags import csrf_token
from django.views import defaults

from cart.cart import Cart
from .models import Order, OrderItem
import requests

from django.http import JsonResponse


# Create your views here.
def start_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')
        room_type = request.POST.get('room_type')
        total_price = 0

        items = []
        string_items_for_req = ' и '.join(items)

        for item in cart:
            product = item['product']
            total_price += product.price * int(item['quantity'])
            items.append(product.slug)

        string_items_for_req = ' and '.join(items)
        id = uuid.uuid4().int

        data = {
            'merchant': settings.OXA_PAY_KEY,
            'amount': total_price,
            'currency': settings.CURRENCY,
            'lifeTime': 20,
            'feePaidByPayer': 0,
            'underPaidCover': 2.5,
            'callbackUrl': 'http://127.0.0.1:8000/cart',
            'returnUrl': 'http://127.0.0.1:8000/cart/success',
            'description': string_items_for_req,
            'orderId': id,
            'email': email
        }
        print(data)

        # Нужно проверить прошла ли оплата
        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email,
                                     phone=phone, date_of_birth=date_of_birth, amount_to_pay=total_price, room_type=room_type)
        print(order)
        print(request.user)

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            print(quantity, product.price)
            price = product.price * quantity
            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

        # print(final.product.description)
        url = 'https://api.oxapay.com/merchants/request'
        response = requests.post(url, data=json.dumps(data))
        result = response.json()

        order.lid = result['trackId']
        order.save()
        print(order.lid)

        # Sent postreq to oxapay

        print(result)
        if result['message'] == 'success':
            return redirect(result['payLink'])
        else:
            return redirect('pay_err')

        # return redirect('myaccount')

    return redirect('cart')


def pay_err(request):
    return render(request, 'order/pay_err.html')

# def start_payment(data):
#     url = 'https://api.oxapay.com/merchants/request'
#     response = requests.post(url, data=json.dumps(data))
#     result = response.json()
#     if result['message'] == 'success':
#         return result
#     else:
#         return redirect('pay_err')
