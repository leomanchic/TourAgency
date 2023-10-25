import json

from django.shortcuts import render, redirect
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

        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email,
                                     phone=phone, date_of_birth=date_of_birth)

        final = None
        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            print(quantity, product.price)
            price = product.price * quantity
            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
            final = item

        print(final.id)
        url = 'https://api.oxapay.com/merchants/request'
        data = start_payment(final.price, email)

        # Sent postreq to oxapay
        response = requests.post(url, data=json.dumps(data))
        result = response.json()
        if result['message'] == 'success':
            return redirect(result['payLink'])
        else:
            return redirect('pay_err')

        # return redirect('myaccount')

    return redirect('cart')

def pay_err(request):
    return render(request, 'order/pay_err.html')
def start_payment(price, email):
    data = {
        'merchant': 'WAFHVV-78Z4FV-MDHGEV-GTXCZ8',
        'amount': price,
        'currency': '1',
        'lifeTime': 20,
        'feePaidByPayer': 0,
        'underPaidCover': 2.5,
        'callbackUrl': 'https://example.com/callback',
        'returnUrl': 'https://example.com/success',
        'description': 'Order #12345',
        'orderId': 'ORD-12345',
        'email': email
    }
    return data
