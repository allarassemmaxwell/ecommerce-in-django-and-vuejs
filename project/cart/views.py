from django.conf import settings
from django.shortcuts import render
from .cart import Cart






# CART DETAIL FUNCTION
def cart_detail(request):
    cart = Cart(request)
    productsstring = ''
    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'], product.thumbnail.url, url, product.num_available)
        productsstring = productsstring + b

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name  = request.user.last_name
        email      = request.user.email
        address    = request.user.userprofile.address
        zipcode    = request.user.userprofile.zipcode
        place      = request.user.userprofile.place
        phone      = request.user.userprofile.phone
    else:
        first_name = last_name = email = address = zipcode = place = phone = ''

    contaxt = {
        'cart': cart,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'address': address,
        'zipcode': zipcode,
        'place': place,
        'phone': phone,
        'pub_key':settings.STRIPE_API_KEY_PUBLISHABLE,
        'productsstring': productsstring
    }
    return render(request, 'cart.html', contaxt)





# SUCCESS MESSAGE AFTER PURCHASING
def success(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'success.html')




# CART FUNCTION
def cart(request):
    return {'cart': Cart(request)}  






