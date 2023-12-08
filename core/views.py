from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
from products.models import Product, Category, City
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm


def frontpage(request):
    products = Product.objects.all()[0:8]
    return render(request, "core/frontpage.html", {'products': products})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})


@login_required
def my_account(request):
    return render(request, 'core/myaccount.html', )


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    cities = City.objects.all()

    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__city__name__contains=active_category)

    query = request.GET.get('query', '')
    if query:

        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query) )
        categories = categories.filter(Q(city__name__icontains=query))
        # print(categories[0].city,categories)


    # print(categories[0].city)#
    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category,
        'cities': cities,
    }
    return render(request, "core/shop.html", context)
