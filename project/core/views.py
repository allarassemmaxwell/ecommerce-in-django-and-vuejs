from urllib import request

from django.shortcuts import render
from store.models import Product, Category


def frontpage(request):
    products = Product.objects.filter()
    context = {
        'products': products
    }
    return render(request, 'frontpage.html', context)




def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})

