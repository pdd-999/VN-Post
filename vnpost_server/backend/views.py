from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import routers, serializers, viewsets, generics

class User_viewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializers_class = User_serializer


class Motorbike_regis_cert_viewset(viewsets.ModelViewSet):
    queryset = Motorbike_regis_cert.objects.all()
    serializer_class = Motorbike_regis_cert_serializer


class Contract_deliverer_viewset(viewsets.ModelViewSet):
    queryset = Contract_deliverer.objects.all()
    serializer_class = Contract_deliverer_serializer


class Contract_desc_viewset(viewsets.ModelViewSet):
    queryset = Contract_desc.objects.all()
    serializer_class = Contract_desc_serializer