import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from cart.cart import Cart
from .models import Product
from order.models import Order, OrderItem
from order.utils import checkout
from order.models import Order




def api_checkout(request):
    cart = Cart(request)
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    first_name  = data['first_name']
    last_name   = data['last_name']
    email       = data['email']
    address     = data['address']
    zipcode     = data['zipcode']
    place       = data['place']
    ordeid      = checkout(
        request,
        first_name,
        last_name,
        email,
        address,
        zipcode,
        place
    )
    paid = True
    if paid == True:
        order = Order.objects.get(pk=ordeid)
        order.paid = True
        order.paid_amount = cart.get_total_cost()
        order.save()
        cart.clear()
    return JsonResponse(jsonresponse)




# ADD PRODUCT TO THE CART
def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id   = data['product_id']
    update       = data['update']
    quantity     = data['quantity']
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)
    return JsonResponse(jsonresponse)



# REMOVE PRODUCT IN THE CART
def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = str(data['product_id'])
    cart = Cart(request)
    cart.remove(product_id)
    return JsonResponse(jsonresponse)



# INCREMENT PRODUCT QUANTITY IN THE CART
def api_increment_quantity(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = str(data['product_id'])
    cart = Cart(request)






