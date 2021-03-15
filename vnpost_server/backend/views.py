from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import routers, serializers, viewsets, generics

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MotorbikeRegisCertViewset(viewsets.ModelViewSet):
    queryset = MotorbikeRegisCert.objects.all()
    serializer_class = MotorbikeRegisCertSerializer


class ContractDelivererViewset(viewsets.ModelViewSet):
    queryset = ContractDeliverer.objects.all()
    serializer_class = ContractDelivererSerializer


class ContractDescViewset(viewsets.ModelViewSet):
    queryset = ContractDesc.objects.all()
    serializer_class = ContractDescSerializer