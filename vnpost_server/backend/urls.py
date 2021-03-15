from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url, include
from .serializers import *
from .views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewset, 'user')
router.register(r'motorbike_regis_cert', MotorbikeRegisCertViewset,'motorbike_regis_cert')
router.register(r'contract_deliverer', ContractDelivererViewset, 'contract_deliverer')
router.register(r'contract_desc', ContractDescViewset, 'contract_desc')

urlpatterns = [
    path('', include(router.urls)),
]
