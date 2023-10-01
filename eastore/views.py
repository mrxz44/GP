from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import *

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

# class LicenseViewSet(mixins.RetrieveModelMixin,
#                      GenericViewSet):
#     queryset = License.objects.all()
#     serializer_class = LicenceSerialiser

    # def qet_queryset(self, request):
    #     account = self.request.query_params.get('mt_account')
    #     print("\n---account:", account)
    #     # queryset = License.objects.filter(mt_account=account)
    #     queryset = License.objects.all()
    #     return queryset

    # @action(methods=['GET'], detail=False)
    # def check_mt_account(self, request):
    #     print("\n----- request:", request, type(request))
    #     # account = request
    #     # account = request.split("/")[-1]
    #     serializer = LicenseViewSet(data=request.data,
    #                                  context={'request': request})
    #     # serializer.is_valid(raise_exception=True)
    #     mt_accounts = License.objects.all()
    #     return mt_accounts
        # return Response({'mt_acc': [m.mt_account for m in mt_accounts]})

class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenceSerialiser