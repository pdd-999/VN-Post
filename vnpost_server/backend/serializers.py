from rest_framework import routers, serializers, viewsets, generics
import django_filters
from django.utils.translation import ugettext_lazy as _
from django_filters.widgets import DateRangeWidget, RangeWidget
import datetime
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import permissions
import os 
from .models import *

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class Motorbike_regis_cert_serializer(serializers.ModelSerializer):
    class Meta:
        model = Motorbike_regis_cert
        fields = ['cert_id', 'province_public_security', 'district_public_security', 'number', 'owner', 'address', 'brand', 'model_code', 'engine', 'chassis', 'color', 'activation_scope', 'plate', 'date_of_expiry', 'upd_date']


class Contract_deliverer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contract_deliverer
        fields = ['deliverer_id','full_name', 'code', 'department', 'email', 'telephone', 'upd_date']


class Contract_desc_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contract_desc
        fields = ['deliverer_id', 'contract_number', 'client_name', 'customer_id', 'plate_number', 'other_doc', 'mrc', 'notes']
