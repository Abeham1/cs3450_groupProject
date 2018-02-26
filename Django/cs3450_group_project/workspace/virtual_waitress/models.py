from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AllowedItems(models.Model):
    name = models.CharField("Item Name", max_length=250)
    units = models.CharField(max_length=50)

class Items(models.Model):
    name = models.ForeignKey(AllowedItems, on_delete=models.CASCASE)
    loc = models.CharField("Item Location", max_length=250)
    qty = models.PositiveIntegerField(default=0, localize=False)
    cost = models.FloatField("Unit Cost", default=0, localize=False)
    expiration = models.DateField("Expiration Date")
    vendor = models.CharField(max_length=250)
