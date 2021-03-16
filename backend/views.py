from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import routers, serializers, viewsets, generics
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
from django.http import HttpResponse, JsonResponse


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CertificationFrontViewset(viewsets.ModelViewSet):
    queryset = CertificationFront.objects.all()
    serializer_class = CertificationFrontSerializer


class CertificationBackViewset(viewsets.ModelViewSet):
    queryset = CertificationBack.objects.all()
    serializer_class = CertificationBackSerializer


class ContractDelivererViewset(viewsets.ModelViewSet):
    queryset = ContractDeliverer.objects.all()
    serializer_class = ContractDelivererSerializer


class ContractDescViewset(viewsets.ModelViewSet):
    queryset = ContractDesc.objects.all()
    serializer_class = ContractDescSerializer


@csrf_exempt 
def upload_file(request):
    if request.method == 'POST':
        card_front = request.FILES['card_front']
        card_back = request.FILES['card_back']
        contract = request.FILES['contract']

        card_front_instance = CertificationFront.objects.create(file = File(card_front.read(), name = card_front.filename))
        card_back_instance = CertificationBack.objects.create(file = File(card_back.read(), name = card_back.filename))
        contract_deliverer_instance = ContractDeliverer.objects.create(file = File(contract_deliverer.read(), name = contract_deliverer.filename))

        consumner = Customer.objects.create()
        consumner.name = card_front_instance.name 
        consumner.save()

        return JsonResponse({
            'success': True,
            'error': None
        })
