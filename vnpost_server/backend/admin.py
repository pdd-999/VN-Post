from django.contrib import admin

# Register your models here.
from .models import Motorbike_regis_cert, Contract_deliverer, Contract_desc

class Motorbike_regis_cert_admin(admin.ModelAdmin):
    fields = ['cert_id', 'province_public_security', 'district_public_security', 'number', 'owner', 'address', 'brand', 'model_code', 'engine', 'chassis', 'color', 'activation_scope', 'plate', 'date_of_expiry', 'upd_date']
    list_display = ['cert_id', 'province_public_security', 'district_public_security', 'number', 'owner', 'address', 'brand', 'model_code', 'engine', 'chassis', 'color', 'activation_scope', 'plate', 'date_of_expiry', 'upd_date']
    search_fields = ['cert_id', 'province_public_security', 'district_public_security', 'number', 'owner', 'address', 'brand', 'model_code', 'engine', 'chassis', 'color', 'activation_scope', 'plate', 'date_of_expiry', 'upd_date']
    list_filter = ['cert_id', 'province_public_security', 'district_public_security', 'number', 'owner', 'address', 'brand', 'model_code', 'engine', 'chassis', 'color', 'activation_scope', 'plate', 'date_of_expiry', 'upd_date']


class Contract_deliverer_admin(admin.ModelAdmin):
    fields = ['deliverer_id','full_name', 'code', 'department', 'email', 'telephone', 'upd_date']
    list_display = ['deliverer_id','full_name', 'code', 'department', 'email', 'telephone', 'upd_date']
    search_fields = ['deliverer_id','full_name', 'code', 'department', 'email', 'telephone', 'upd_date']
    list_filter = ['deliverer_id','full_name', 'code', 'department', 'email', 'telephone', 'upd_date']


class Contract_desc_admin(admin.ModelAdmin):
    fields = ['deliverer_id', 'contract_number', 'client_name', 'customer_id', 'plate_number', 'other_doc', 'mrc', 'notes']
    list_display = ['deliverer_id', 'contract_number', 'client_name', 'customer_id', 'plate_number', 'other_doc', 'mrc', 'notes']
    search_fields = ['deliverer_id', 'contract_number', 'client_name', 'customer_id', 'plate_number', 'other_doc', 'mrc', 'notes']
    list_filter = ['deliverer_id', 'contract_number', 'client_name', 'customer_id', 'plate_number', 'other_doc', 'mrc', 'notes']

admin.site.register(Motorbike_regis_cert, Motorbike_regis_cert_admin)
admin.site.register(Contract_deliverer, Contract_deliverer_admin)
admin.site.register(Contract_desc, Contract_desc_admin)