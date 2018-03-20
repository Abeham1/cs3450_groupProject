from django.contrib import admin

from .models import AllowedItems, Items, RestaurantName

# Register your models here.
admin.site.register(RestaurantName)
admin.site.register(AllowedItems)
admin.site.register(Items)
