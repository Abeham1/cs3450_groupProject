from django.contrib import admin

from .models import AllowedItems, Items

# Register your models here.
admin.site.register(AllowedItems)
admin.site.register(Items)