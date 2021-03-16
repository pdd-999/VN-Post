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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CertificationFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationFront
        fields = ['id', 'province_public_security', 'district_public_security', 'number']


class CertificationBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationBack
        fields = ['id', 'owner', 'address', 'brand', 'model_code', 'engine', 'chassis', 'color', 'activation_scope', 'plate', 'date_of_expiry', 'upd_date']

class ContractDelivererSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractDeliverer
        fields = ['id','full_name', 'code', 'department', 'email', 'telephone', 'upd_date']


class ContractDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractDesc
        fields = ['id', 'contract_id', 'contract_number', 'client_name', 'customer_id', 'plate_number', 'other_doc', 'mrc', 'notes']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'cert', 'contract_deliverer', 'contract_desc']
