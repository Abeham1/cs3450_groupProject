from pprint import pprint

from django.shortcuts import render
import json
from virtual_waitress.models import RestaurantName, Order, OrderItem, Menu, Number
import datetime

#https://stackoverflow.com/questions/455580/json-datetime-between-python-and-javascript/
json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)

def manager(request):
    result = RestaurantName.objects.all()
    myresult = Order.objects.all()
    #for x in myresult:
    #    x.dateCreated = strftime(x.dateCreated)
    #print(myresult)

    
    mylist = (list(myresult.values()))
    #myresult = Order.objects.filter(str(Order.objects.datetime))
    #myresult = Order.objects.get(pk=1).total
    #mylist = myresult
    #myresult = str(Order.objects.get(pk=1).dateCreated)
    #mylist = myresult


    lst = (list(result.values())) 
    context = {
        'activePage': 'manager',
        'restaurantName': json.dumps(lst),
        'tableData': json.dumps(mylist)
    }

    #use this as a starting point to delete from the database
    #Number.objects.filter(number = 1).delete()

    # Removes menuitems from the admin page
    if 'removeItem' in request.POST:
        badItem = request.POST.get('removeItem')
        Menu.objects.filter(menuItem = badItem).delete()
        #Menu.objects

    return render(request, 'virtual_waitress/manager.html', context)


def cook(request):
    openOrders = Order.objects.filter(orderitem__ready=False)
    pprint(openOrders.values())

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
    myresult = Menu.objects.all()
    mylist = (list(myresult.values()))
    lst = (list(result.values()))
    context = {
        'activePage': 'menu',
        'restaurantName': json.dumps(lst),
        'comboItemsMenu': json.dumps(mylist),
    }
    return render(request, 'virtual_waitress/menu.html', context)
