from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import PersonForm


def from_app(request):
    return HttpResponse("This is http response from an app")


def second_function(request):
    return HttpResponse("This is http response from an app with second function")


def show_index_page(request):
    return render(request, 'products/index.html')


def second_page(request):
    return render(request, 'products/second.html')


def get_products(request):
    products_django = Product.objects.all()
    context = {
        "products": products_django
    }
    return render(request, 'products/getProducts.html', context)


def get_person_form(request):
    form_django = PersonForm()
    context = {
        'form': form_django
    }
    return render(request, 'products/get_person_form.html', context)
