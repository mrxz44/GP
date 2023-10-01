import io
from rest_framework.serializers import Serializer, FileField
from rest_framework import serializers
from .models import *

class LicenceSerialiser(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ("robot_name", "is_valid", "price", "mt_account")
