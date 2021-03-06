import datetime
from django.db import models


# Create your models here.
class AllowedItems(models.Model):
    name = models.CharField("Item Name", max_length=250)
    units = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Allowable Inventory Item"


class Items(models.Model):
    itemType = models.ForeignKey(AllowedItems, on_delete=models.CASCADE)
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


class Order(models.Model):
    dateCreated = models.DateTimeField()
    ready = models.BooleanField(default=False)
    total = models.FloatField()
    orderNumber = models.IntegerField()
    table = models.CharField(default='counter', max_length=50)

    def __str__(self):
        return str(self.orderNumber)

    class Meta:
        verbose_name = "Order"


class Number(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = "Number"


class Menu(models.Model):
    menuItem = models.CharField(max_length=60)
    menuDescription = models.CharField(max_length=400)
    menuPrice = models.FloatField()

    def __str__(self):
        return str(self.menuItem)

    class Meta:
        verbose_name = "Menu"


class Review(models.Model):
    menuItem = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    starRating = models.FloatField()
    review = models.CharField(max_length=250)

    def __str__(self):
        return str(self.review)

    class Meta:
        verbose_name = "Review"


class Entry(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Menu, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    note = models.TextField("Customer Notes", blank=True)
    ready = models.BooleanField("Food Ready", default=False)
    foodName = models.CharField(max_length=60)

    def __str__(self):
        return str(self.qty) + "x " + str(self.food) + " for order " + str(self.order)

    class Meta:
        verbose_name = "Order Item"
