from pprint import pprint
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import json
from virtual_waitress.models import RestaurantName, Order, Entry, Menu, Number, Review
from virtual_waitress.forms import NewMenuItem, ReviewForm, OrderForm, OrderItemForm, CompleteOrderItem, CompleteOrder
from django.forms import formset_factory
import datetime

#https://stackoverflow.com/questions/455580/json-datetime-between-python-and-javascript/
json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)

def manager(request):
    result = RestaurantName.objects.all()
    myresult = Order.objects.all()
    mymyresult = Menu.objects.all()
    mymylist = (list(mymyresult.values()))
    mylist = (list(myresult.values()))
    lst = (list(result.values()))
    context = {
        'activePage': 'manager',
        'comboItemsMenu': json.dumps(mymylist),
        'restaurantName': json.dumps(lst),
        'tableData': json.dumps(mylist),
    }
	
    #use this as a starting point to delete from the database
    #Number.objects.filter(number = 1).delete()

    # Removes menuitems from the admin page
    if 'removeItem' in request.POST:
        badItem = request.POST.get('removeItem')
        Menu.objects.filter(menuItem = badItem).delete()
        #Menu.objects

    # Adds a new meun item from the manager page
    if 'newMenuItemSubmit' in request.POST:
        form = NewMenuItem(request.POST)
        print(form)
        print(form.is_valid())
        #print(form.cleaned_data['newItem'])
        if form.is_valid():
            num = Menu()
            num.menuItem = form.cleaned_data['menuItem']
            num.menuDescription = form.cleaned_data['menuDescription']
            num.menuPrice = form.cleaned_data['menuPrice']
            num.save()
            print(num)
        #num.save()
        # print('item')
        # print(request.POST.get('newItem'))
        # print('description')
        # print(request.POST.get('newItemDescription'))
        # print('price')
        # print(request.POST.get('newItemPrice'))
        # print('object')


    return render(request, 'virtual_waitress/manager.html', context)


def cook(request):
    open_orders = Order.objects.filter(ready=False).order_by('dateCreated')

    restaurant_names = list(RestaurantName.objects.all().values())

    # if request.method == 'POST':
    #     entry_form = CompleteOrderItem(request.POST)
    #     order_form = CompleteOrder(request.POST)
        
    #     if entry_form.is_valid():
    #         order_item = entry_form.save(commit=False)
    #         print(order_item)
    #         order_item.ready = True
    #         order_item.save()
        
    #     if order_form.is_valid():
    #         order = order_form.save(commit=False)
    #         order.ready = True
    #         order.save()

    #     return HttpResponseRedirect(reverse('virtual_waitress:cook'))

    # entry_form = CompleteOrderItem()
    # order_form = CompleteOrder()

    context = {
        'activePage': 'cook',
        'restaurantName': json.dumps(restaurant_names),
        'orders': open_orders,
        # 'orderForm':order_form,
        # 'entryForm':entry_form,
    }
    return render(request, 'virtual_waitress/cook_view.html', context)


def update_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)

    if request.method != 'POST':
        return HttpResponseNotAllowed(request)

    entry.ready = True
    entry.save()
    
    return HttpResponseRedirect(reverse('virtual_waitress:cook'))

def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if request.method != 'POST':
        return HttpResponseNotAllowed(request)

    order.ready = True
    order.save()
    
    return HttpResponseRedirect(reverse('virtual_waitress:cook'))

def review(request):
    #1. get order number
    #2. get queryset of all orderItems relating to order number
    #3. get queryset of all foodItems mentioned by orderItems
    #3.a turn queryset into array
    #3.b get length of array
    #3.c for loop get menu item for each id in array and push to new dynamic array
    #4. Pass to javascript as an array of objects
    #5. Generate Orderlistreview table. One row for each element in queryset
    #6. Get form data and save to model -- This is the hard part.

    numReviews = Review.objects.all()
    restaurantNames = list(RestaurantName.objects.all().values())
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(form.errors)
    else:
        form = ReviewForm()
    context = {
        'activePage': 'review',
        'form' : form,
        'restaurantName': json.dumps(restaurantNames),
    }
    if not numReviews:
        return render(request, 'virtual_waitress/customer_review.html', context)
    else:
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
    mymyresult = Order.objects.all()
    mymylist = (list(mymyresult.values()))
    mylist = (list(myresult.values()))
    lst = (list(result.values()))
    mySize = 2
    context = {
        'activePage': 'menu',
        'restaurantName': json.dumps(lst),
        'comboItemsMenu': json.dumps(mylist),
        'orderList': json.dumps(mymylist),
    }

    #form = OrderForm()
    #print(form)
    #orderItemFormSet = formset_factory(OrderItemForm, extra=2)
    #formset = orderItemFormSet()
    #for form in formset:
    #    print(form.as_table())
    #print(orderItemFormSet)
    #print(orderItemFormSet.is_valid())

    #orderForm = OrderForm(prefix='order')
    orderItemForm = OrderItemForm()

    #print(orderForm)
    print(orderItemForm)
    #print(orderItemForm.is_valid())
    if 'placeTestOrder' in request.POST:
        orderForm = OrderForm(request.POST, prefix='order')
        orderItemForm = OrderItemForm(request.POST, prefix='orderItem')

        #print(orderForm)
        #print(orderItemForm)
        #print(orderItemForm.is_valid())
        #print(orderItemForm.is_valid())
        
        if orderForm.is_valid() and Order.objects.filter(orderNumber=orderForm.cleaned_data['orderNumber']).exists() == False:
            num = Order()
            
            num.dateCreated = datetime.datetime.now()
            num.ready = False
            num.total = orderForm.cleaned_data['total']
            num.orderNumber = orderForm.cleaned_data['orderNumber']
            num.table = orderForm.cleaned_data['table']
            
            num.save()
        elif orderForm.is_valid():
            num = Order.objects.get(orderNumber=orderForm.cleaned_data['orderNumber'])
            num.total += orderForm.cleaned_data['total']
            num.save()

        if orderItemForm.is_valid() and (orderItemForm.cleaned_data['qty1'] != 0) and (orderItemForm.cleaned_data['food1'] != 'empty'):
            Item = orderItemForm.cleaned_data['food1']
            num1 = Entry(
                order = num,
                food = Menu.objects.get(menuItem=Item),
                qty = orderItemForm.cleaned_data['qty1'],
                note = orderItemForm.cleaned_data['note1']
            )
            num1.save()

        if orderItemForm.is_valid() and (orderItemForm.cleaned_data['qty2'] != 0) and (orderItemForm.cleaned_data['food2'] != 'empty'):
            Item = orderItemForm.cleaned_data['food2']
            num2 = Entry(
                order = num,
                food = Menu.objects.get(menuItem=Item),
                qty = orderItemForm.cleaned_data['qty2'],
                note = orderItemForm.cleaned_data['note2']
            )
            num2.save()

        if orderItemForm.is_valid() and (orderItemForm.cleaned_data['qty3'] != 0) and (orderItemForm.cleaned_data['food3'] != 'empty'):
            Item = orderItemForm.cleaned_data['food3']
            num3 = Entry(
                order = num,
                food = Menu.objects.get(menuItem=Item),
                qty = orderItemForm.cleaned_data['qty3'],
                note = orderItemForm.cleaned_data['note3']
            )
            num3.save()

        if orderItemForm.is_valid() and (orderItemForm.cleaned_data['qty4'] != 0) and (orderItemForm.cleaned_data['food4'] != 'empty'):
            Item = orderItemForm.cleaned_data['food4']
            num4 = Entry(
                order = num,
                food = Menu.objects.get(menuItem=Item),
                qty = orderItemForm.cleaned_data['qty4'],
                note = orderItemForm.cleaned_data['note4']
            )
            num4.save()

        if orderItemForm.is_valid() and (orderItemForm.cleaned_data['qty5'] != 0) and (orderItemForm.cleaned_data['food5'] != 'empty'):
            Item = orderItemForm.cleaned_data['food5']
            num5 = Entry(
                order = num,
                food = Menu.objects.get(menuItem=Item),
                qty = orderItemForm.cleaned_data['qty5'],
                note = orderItemForm.cleaned_data['note5']
            )

            num5.save()








        #     # num2.order = Order.objects.get(num.orderNumber)
        #     # num2.food = Menu.objects.get(menuItem='Drink')
        #     # num2.qty = form.cleaned_data['qty']
        #     # num2.note = form.cleaned_data['note']
        #     # num2.ready = False

        #     print(num)

    return render(request, 'virtual_waitress/menu.html', context)
