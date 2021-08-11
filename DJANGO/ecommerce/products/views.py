from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def from_app(request):
    return HttpResponse("This is http response from an app")


def second_function(request):
    return HttpResponse("This is http response from an app with second function")


def show_index_page(request):
    return render(request, 'products/index.html')


def second_page(request):
    return render(request, 'products/second.html')


def get_products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'products/getProducts.html', context)


