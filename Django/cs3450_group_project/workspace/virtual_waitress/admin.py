from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(RestaurantName)
admin.site.register(AllowedItems)
admin.site.register(Items)
admin.site.register(Entry)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Number)
admin.site.register(Review)

