from django.urls import path

from . import views

app_name = "virtual_waitress"

urlpatterns = [
    # /virtual_waitress/manager/
    path('manager/', views.manager, name='manager'),

    # /virtual_waitress/cook/
    path('cook/', views.cook, name='cook'),

    path('update/entry/<int:entry_id>/', views.update_entry, name='entry_update'),
    path('update/order/<int:order_id>/', views.update_order, name='order_update'),

    # /virtual_waitress/review/
    path('review/', views.review, name='review'),

    # /virtual_waitress/inventory/
    path('inventory/', views.inventory, name='inventory'),

    # /virtual_waitress/
    path('', views.menu, name='menu'),

    # returning to menu from any other page
    path('menu/', views.menu, name='menu'),
]
