from django.shortcuts import render, redirect
from django.db.models import Q
from listings.models import Item
from .models import *

from . import utils
from . import payments

# Create your views here.
def cart(request):

    ctxt = {}

    try:
        active_cart = Cart.objects.get(status='adding')
        ctxt = utils.getCartSummary(active_cart)

        empty = False
        if(ctxt['cart_total'] == 0.0):
            empty = True

        ctxt['empty'] = empty

    except:
        pass

    return render(request, 'orders/cart.html', context = ctxt)

def addToCart(request, item_id):

    try:
        bag = Cart.objects.get(Q(status = 'adding') & Q(user = request.user))
    except:
        bag = Cart()
        bag.user = request.user
        bag.save()

    item = Item.objects.get(id = item_id)
    c_item = CartItem()
    c_item.item = item
    c_item.cart = bag
    c_item.save()

    return redirect('home')

def checkout(request, chain):
    # try:
        active_cart = Cart.objects.get(Q(status = 'adding') & Q(user = request.user))
        active_cart_details = utils.getCartSummary(active_cart)
        cart_total = active_cart_details['cart_total']
        # active_cart.save()

        active_cart.chain = 1

        if(chain < 3):
            active_cart.chain = chain

        print('making a payment request')
        active_cart.unique_code = payments.register_transaction(active_cart, cart_total, chain)
        print('code: '+active_cart.unique_code)
        active_cart.status = 'check'

        active_cart.save()

        return redirect('home')


    # except:
    #     pass
    #
        return redirect('home') # TODO: Render a page for displaying the checkout code

def all_orders(request):
    utils.update_orders(request.user)

    carts_query = Cart.objects.filter(~Q(status = 'adding') & Q(user = request.user))

    carts = []

    for cart in carts_query:
        cart_rep = {}
        cart_rep['status'] = cart.status
        cart_rep['unique_code'] = cart.unique_code
        cart_rep['chain'] = cart.chain

        cart_details = utils.getCartSummary(cart)
        cart_rep['cart_items'] = cart_details['cart_items']
        cart_rep['cart_total'] = cart_details['cart_total']

        carts.append(cart_rep)

    carts.reverse()

    ctxt = {
        'carts': carts,
    }

    return render(request, 'orders/all_orders.html', context = ctxt)
