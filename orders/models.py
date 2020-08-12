from django.db import models
from django.contrib.auth.models import User

from listings.models import Item

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(max_length=15) #Adding, Checked, Confirmed
    unique_code = models.CharField(max_length=50, default='')

    def __str__(self):
        try:
            return self.user.username + ' - ' + str(self.id)
        except:
            return 'Deleted User - ' + str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)

    def __str__(self):
        try:
            return 'Cart ' + str(self.cart.id) + ' - ' + 'Item ' + str(self.item.id)
        except:
            return 'Either the cart or the item no longer exists'
