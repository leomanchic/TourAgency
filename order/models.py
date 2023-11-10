from django.contrib.auth.models import User
from django.db import models

from products.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
    date_of_birth = models.DateField(blank=False, null=True)
    phone = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False, null=True)
    paid_amount = models.IntegerField(blank=True, null=True)
    amount_to_pay = models.IntegerField(blank=True, null=True)
    lid = models.PositiveBigIntegerField(blank=False,null=True)


#
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    # paid = models.ForeignKey(Order, related_name='orderitem', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
