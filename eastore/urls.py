from django.views.generic.base import TemplateView
from django.urls import path
from .views import *


urlpatterns = [
    path('', test_main, name='main'),
    path('1/', test_1, name='test1'),
    path('2/', test_2, name='test2'),
    path('3/', test_3, name='test3'),
    path('4/', test_4, name='test4'),

]