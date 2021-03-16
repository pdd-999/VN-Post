from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url, include
from .serializers import *
from .views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewset, 'user')
router.register(r'cert_front', CertificationFrontViewset,'certification_front')
router.register(r'cert_back', CertificationBackViewset,'certification_back')
# router.register(r'cert_front/upload', call_predict_card_api,'certification_front')

router.register(r'contract_deliverer', ContractDelivererViewset, 'contract_deliverer')
router.register(r'contract_desc', ContractDescViewset, 'contract_desc')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', upload_file, name='upload'),
]
