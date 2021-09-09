from urllib import request
from django.shortcuts import render
from store.models import Product, Category





# FRONT PAGE FUNCTION
def frontpage(request):
    products = Product.objects.filter(is_featured=True)
    featured_categories = Category.objects.filter(is_featured=True)
    context = {
        'products': products,
    }
    return render(request, 'frontpage.html', context)






# CONTACT FUNCTION
def contact(request):
    return render(request, 'contact.html', {})





# ABOUT FUNCTION
def about(request):
    return render(request, 'about.html', {})












