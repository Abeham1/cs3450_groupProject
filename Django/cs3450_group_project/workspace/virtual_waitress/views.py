from pprint import pprint
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render
import json
from virtual_waitress.models import RestaurantName, Order, OrderItem, Menu, Number
from virtual_waitress.forms import NewMenuItem
import datetime


def manager(request):
    context = {
        'activePage': 'manager'
    }

    # use this as a starting point to delete from the database
    # Number.objects.filter(number = 1).delete()

    # Removes menuitems from the admin page
    if 'removeItem' in request.POST:
        bad_item = request.POST.get('removeItem')
        Menu.objects.filter(menuItem=bad_item).delete()
        # Menu.objects

    # Adds a new meun item from the manager page
    if 'newMenuItemSubmit' in request.POST:
        form = NewMenuItem(request.POST)
        print(form)
        print(form.is_valid())
        # print(form.cleaned_data['newItem'])
        if form.is_valid():
            num = Menu()
            num.menuItem = form.cleaned_data['menuItem']
            num.menuDescription = form.cleaned_data['menuDescription']
            num.menuPrice = form.cleaned_data['menuPrice']
            num.save()
            print(num)
            # num.save()
            # print('item')
            # print(request.POST.get('newItem'))
            # print('description')
            # print(request.POST.get('newItemDescription'))
            # print('price')
            # print(request.POST.get('newItemPrice'))
            # print('object')

    return render(request, 'virtual_waitress/manager.html', context)


def cook(request):
    openOrders = Order.objects.filter(orderitem__ready=False)
    pprint(openOrders)
    food = OrderItem.objects.filter()
    pprint(food)

    restaurantNames = list(RestaurantName.objects.all().values())
    context = {
        'activePage': 'cook',
        'restaurantName': json.dumps(restaurantNames),

    }
    return render(request, 'virtual_waitress/cook_view.html', context)


def review(request):
    context = {
        'activePage': 'review'
    }
    return render(request, 'virtual_waitress/customer_review.html', context)


def inventory(request):  # To send model data from Database to Javascript/Template
    # For multiple, or complex data types, 
    # you have a queryset. This must be translated into JSON data
    # 1. Save the queryset to a variable.
    result = RestaurantName.objects.all()
    # 2. call the .values() function on your variable to get data contents.
    #  Use list() to to put it into serializable format
    lst = (list(result.values()))  #
    context = {
        'activePage': 'inventory',
        # 3. JSON.dumps converts previous variable to JSON
        # note: when bringing variable into javascript, escapejs filter 
        # must be used in tempalte
        'restaurantName': json.dumps(lst),
        # For single dataobjects, just create variable and pass in by Primary Key
        'foo': RestaurantName.objects.get(pk=1),
    }
    return render(request, 'virtual_waitress/inventory.html', context)


def menu(request):
    result = RestaurantName.objects.all()
    lst = (list(result.values()))
    context = {
        'activePage': 'menu',
        'restaurantName': json.dumps(lst),
    }
    return render(request, 'virtual_waitress/menu.html', context)
