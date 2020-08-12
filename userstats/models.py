from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserStat(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    google_id = models.CharField(max_length=500, blank=True, default="")
    shipping_address = models.CharField(max_length=1000)
    # city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        try:
            return self.user.username
        except:
            return 'Deleted User'
