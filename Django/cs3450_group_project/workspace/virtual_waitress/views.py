from django.shortcuts import render

def index (request):
    context = {
        'activePage':'menu'
    }
    return render(request, 'virtual_waitress/menu.html', context)

def manager (request):
    context = {
        'activePage':'manager'
    }
    return render(request, 'virtual_waitress/manager.html', context)

def cook (request):
    context = {
        'activePage':'cook'
    }
    return render(request, 'virtual_waitress/cook_view.html', context)

def review (request):
    context = {
        'activePage':'review'
    }
    return render(request, 'virtual_waitress/customer_review.html', context)

def inventory (request):
    context = {
        'activePage':'inventory',
        'resturantName': 'Welcome To Test!'
    }
    return render(request, 'virtual_waitress/inventory.html', context)

def menu (request):
    context = {
        'activePage':'menu'
    }
    return render(request, 'virtual_waitress/menu.html', context)