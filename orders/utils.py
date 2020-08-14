from django.shortcuts import render, redirect
from django.db.models import Q
from listings.models import Item
from .models import *
from django.conf import settings

import requests
import json

def getCartSummary(active_cart):
    cart_items = []
    cart_total = 0.0

    try:
        cart_items_query = CartItem.objects.filter(cart = active_cart)

        for cart_item in cart_items_query:
            cart_items.append(cart_item.item)
            cart_total += cart_item.item.price

    except:
        pass

    ctxt = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }

    return ctxt

def update_orders(user):
    base_url = settings.CRYPTOPAY_URL
    req_url = base_url + 'transactions/confirm/'
    req_key = settings.CRYPTOPAY_API_KEY

    req_data = {
        "key": req_key,
        "customer_email": user.email
    }

    res = (requests.get(req_url, json = req_data)).json()
    confirmed_carts = res['confirmed_transactions']

    print(confirmed_carts)

    checked_carts = Cart.objects.filter(Q(user = user) & Q(status = 'check'))
    print(checked_carts)

    for cart in checked_carts:
        print(cart.unique_code)
        if(cart.unique_code in confirmed_carts):
            print(cart.unique_code)
            cart.status = 'confirmed'
            cart.save()
