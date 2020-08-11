from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=20)
    picture =models.ImageField(upload_to='listings', default=None)
    price = models.FloatField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.Category.name + ' - ' + self.name
