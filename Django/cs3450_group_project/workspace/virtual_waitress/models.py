from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AllowedItems(models.Model):
    name = models.CharField("Item Name", max_length=250)
    units = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Allowable Inventory Item"

class Items(models.Model):
    name = models.ForeignKey(AllowedItems, on_delete=models.CASCADE)
    loc = models.CharField("Item Location", max_length=250)
    qty = models.PositiveIntegerField(default=0)
    cost = models.FloatField("Unit Cost", default=0)
    expiration = models.DateField("Expiration Date")
    vendor = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Inventory Item"
        

class RestaurantName(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Restaurant Name"