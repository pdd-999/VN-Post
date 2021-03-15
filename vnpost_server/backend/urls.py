from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url, include
from .serializers import *
from .views import *

router = routers.DefaultRouter()
router.register(r'user', User_viewset, 'user')
router.register(r'motorbike_regis_cert', Motorbike_regis_cert_viewset,'motorbike_regis_cert')
router.register(r'contract_deliverer', Contract_deliverer_viewset, 'contract_deliverer')
router.register(r'contract_desc', Contract_desc_viewset, 'contract_desc')

urlpatterns = [
    path('', include(router.urls)),
]
