from django.contrib import admin
from django.urls import path, include
from core.views import frontpage, shop, signup
from products.views import product
from cart.views import add_to_cart, cart, checkout
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('core.urls')),
                  path('cart/', include('cart.urls')),
                  path("admin/", admin.site.urls),
path("order/", include('order.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
