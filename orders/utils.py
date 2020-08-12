from django.shortcuts import render, redirect
from django.db.models import Q
from listings.models import Item
from .models import *

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
