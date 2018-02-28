from django.shortcuts import render_to_response

def cook (request):
    return render_to_response('virtual_waitress/cook_view.html')

def review (request):
    return render_to_response('virtual_waitress/customer_review.html')

def inventory (request):
    return render_to_response('virtual_waitress/inventory.html')