# from __future__ import unicode_literals
import datetime

from django.db import models
from django.db.models import CASCADE


# Create your models here.
class AllowedItems(models.Model):
    name = models.CharField("Item Name", max_length=250)
    units = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Allowable Inventory Item"


class Items(models.Model):
    itemType = models.ForeignKey(AllowedItems, on_delete=CASCADE)
    loc = models.CharField("Item Location", max_length=250)
    qty = models.PositiveIntegerField(default=0)
    cost = models.FloatField("Unit Cost", default=0)
    expiration = models.DateField("Expiration Date")
    vendor = models.CharField(max_length=250)

    def __str__(self):
        return str(self.itemType)

    class Meta:
        verbose_name = "Inventory Item"


class RestaurantName(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Restaurant Name"


class Menu(models.Model):
    menuItem = models.CharField(max_length=60)
    menuDescription = models.CharField(max_length=400)
    menuPrice = models.FloatField()

    def __str__(self):
        return str(self.menuItem)

    class Meta:
        verbose_name = "Menu"


class Order(models.Model):
    dateCreated = models.DateTimeField()
    ready = models.BooleanField(default=False)
    total = models.FloatField()
    orderNumber = models.IntegerField()

    def __str__(self):
        return str(self.orderNumber)

    class Meta:
        verbose_name = "Order"
