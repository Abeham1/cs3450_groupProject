from django.contrib import admin

from .models import AllowedItems, Items, RestaurantName, Menu

# Register your models here.
admin.site.register(RestaurantName)
admin.site.register(AllowedItems)
admin.site.register(Items)
admin.site.register(Menu)
