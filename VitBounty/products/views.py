
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product



def productss(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def new_product(request):
    return HttpResponse("New Products are here, you found !")







