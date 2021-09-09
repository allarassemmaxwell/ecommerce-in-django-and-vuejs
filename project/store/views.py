from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
import random
from .models import *
from cart.cart import Cart






# MENU CATEGORY(CONTEXT PROCCESSORS)
def menu_category(request):
    menu_categories = Category.objects.filter(parent=None)
    return {'menu_categories': menu_categories}





# SEARCH PRODUCTS FUNCTION
def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )
    template = 'search.html'
    context = {
        'query': query,
        'products': products
    }
    return render(request, template, context)





# PRODUCT DETAILS FUNCTION
def product_detail(request, category_slug, slug):
    template     = 'product_detail.html'
    product      = get_object_or_404(Product, slug=slug)
    # ADD REVIEW PRODUCT 
    if request.method == 'POST' and request.user.is_authenticated:
        stars   = request.POST.get('stars')
        content = request.POST.get('content')
        review  = ProductReview.objects.create(
            product=product, 
            user=request.user, 
            stars=stars, 
            content=content
        )
        return redirect('product_detail', category_slug=category_slug, slug=slug)
    related_products = list(product.category.products.filter(parent=None).exclude(id=product.id))
    if len(related_products) >= 3:
        related_products = random.sample(related_products, 3)
    imagesstring = "{'thumbnail': '%s', 'image': '%s'}," % (product.thumbnail.url, product.image.url)
    
    if product.parent:
        return redirect('product_detail', category_slug=category_slug, slug=product.parent.slug)
    
    for image in product.images.all():
        imagesstring = imagesstring + ("{'thumbnail': '%s', 'image': '%s'}," % (image.thumbnail.url, image.image.url))

    cart = Cart(request)
    if cart.has_product(product.id):
        product.in_cart = True

    context = {
        'product': product,
        'imagesstring': imagesstring,
        'related_products': related_products
    }
    return render(request, template, context)





# CATEGORY DETAILS FUNCTION
def category_detail(request, slug):
    template = 'category_detail.html'
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(parent=None)
    context = {
        'category': category,
        'products': products
    }
    return render(request, template, context)







