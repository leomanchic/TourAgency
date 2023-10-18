from django.urls import path
from core.views import frontpage, shop, signup, my_account
from django.contrib.auth import views
from products.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path("shop/", shop, name='shop'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path("shop/<slug:slug>/", product, name='product'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('myaccount/',my_account,name='myaccount')
]
