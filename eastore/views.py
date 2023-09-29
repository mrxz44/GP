from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
def test_main(request):
    response = render(request, 'eastore/base_template.html',)
    # response.status_code = 500
    return response

def test_1(request):
    response = render(request, 'eastore/robot_details_template.html',)
    # response.status_code = 500
    return response

def test_2(request):
    response = render(request, 'eastore/robots_all_template.html',)
    # response.status_code = 500
    return response

def test_3(request):
    response = render(request, 'eastore/checkout_template.html',)
    # response.status_code = 500
    return response

def test_4(request):
    response = render(request, 'eastore/cart_template.html',)
    # response.status_code = 500
    return response