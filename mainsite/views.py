from django.shortcuts import render
from django.db.models import Q

from listings.models import *
from orders.models import *

# Create your views here.
def HomePage(request):

    ctxt = {}
    cats = Category.objects.all()

    listings = []

    for cat in cats:
        items = Item.objects.filter(Category = cat)
        listings.append(
            {
                'category': cat,
                'items': items,
            }
        )

    ctxt['listings'] = listings
    cart_items = []

    try:
        cart_items_query = CartItem.objects.filter(cart = Cart.objects.get(Q(user = request.user) & Q(status='adding')))

        for c in cart_items_query:
            # print(c.item.id)
            cart_items.append(c.item.id)
    except:
        pass

    # print(cart_items)

    ctxt['cart_items'] = cart_items

    return render(request, 'mainsite/index.html', context = ctxt)
