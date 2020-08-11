from django.shortcuts import render

from listings.models import *

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

    return render(request, 'mainsite/index.html', context = ctxt)
