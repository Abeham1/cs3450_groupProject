from django.urls import path

from . import views

app_name = "virtual_waitress"

urlpatterns = [
    # /virtual_waitress/manager/
    path('manager/', views.manager, name='manager'),

    # /virtual_waitress/cook/
    path('cook/', views.cook, name='cook'),

    # /virtual_waitress/review/
    path('review/', views.review, name='review'),

    # /virtual_waitress/inventory/
    path('inventory/', views.inventory, name='inventory'),

    # /virtual_waitress/
    path('', views.menu, name='menu'),
]