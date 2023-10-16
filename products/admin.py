from django.contrib import admin

# Register your models here.

from .models import City, Category,Product

admin.site.register(City)
admin.site.register(Product)
admin.site.register(Category)