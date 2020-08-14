import requests
import json

from django.conf import settings

from . models import *

def register_transaction(cart, cart_total, chain):
    print('function called')
    base_url = settings.CRYPTOPAY_URL
    req_url = base_url + 'transactions/register/'

    req_key = settings.CRYPTOPAY_API_KEY

    email = cart.user.email

    # cart_total = 0.0
    # cart_items = CartItem.objects.filter(cart = cart)
    #
    # for cart_item in cart_items:
    #     cart_total += cart_item.item.price

    req_data = {
        "chain": chain,
        "key": req_key,
        "customer_email": email,
        "amount": int(cart_total),
    }

    print('Making a request with the data: '+str(req_data))
    print('URL: '+req_url)
    res = requests.post(req_url, json=req_data)
    # print('Response data: ' +str(res))

    x = res.json()

    print(x)
    unique_code = x['checkout_code']

    # unique_code = 'xyz'

    return unique_code
