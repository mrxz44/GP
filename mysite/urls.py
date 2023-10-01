"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from eastore.views import *
from django.conf.urls.static import static
from mysite import settings
from rest_framework import routers

router_s = routers.DefaultRouter()
router_s.register(r'license/(?P<mt_account>[^/.]+)', LicenseViewSet, basename="license")
print(router_s.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("eastore.urls")),
    path('api/v1/', include(router_s.urls)),
]

