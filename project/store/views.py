from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.





def menu_category(request):
    menu_categories = Category.objects.all()
    return {'menu_categories': menu_categories}


    
def product_detail(request, category_slug, slug):
    template = 'product_detail.html'
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, template, context)




def category_detail(request, slug):
    template = 'category_detail.html'
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    context = {
        'category': category,
        'products': products
    }
    return render(request, template, context)