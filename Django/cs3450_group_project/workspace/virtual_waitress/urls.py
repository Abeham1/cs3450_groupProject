from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^manager/$', views.manager, name='manager'),
    url(r'^cook/$', views.cook, name='cook_view'),
    url(r'^review/$', views.review, name='customer_review'),
    url(r'^inventory/$', views.inventory, name='inventory'),
    url(r'^menu/$', views.menu, name='menu'),
]