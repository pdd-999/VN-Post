from django.contrib import admin

# Register your models here.
from .models import CertificationFront, CertificationBack, ContractDeliverer, ContractDesc, Customer

class CertificationFrontAdmin(admin.ModelAdmin):
    fields = ['id', 'province_public_security', 'district_public_security', 'number']
    list_display = ['id', 'province_public_security', 'district_public_security', 'number']
    search_fields = ['id', 'province_public_security', 'district_public_security', 'number']
    list_filter = ['id', 'province_public_security', 'district_public_security', 'number']


class CertificationBackAdmin(admin.ModelAdmin):
    fields = ['id', 'owner', 'address', 'brand', 'model_code', 'engine', 'chassis', 'color', 'activation_scope', 'plate', 'date_of_expiry']
    list_display = ['id', 'owner', 'address', 'brand', 'model_code', 'engine', 'chassis', 'color', 'activation_scope', 'plate', 'date_of_expiry']
    search_fields = ['id', 'owner', 'address', 'brand', 'model_code', 'engine', 'chassis', 'color', 'activation_scope', 'plate', 'date_of_expiry']
    list_filter = ['id', 'owner', 'address', 'brand', 'model_code', 'engine', 'chassis', 'color', 'activation_scope', 'plate', 'date_of_expiry']


class ContractDelivererAdmin(admin.ModelAdmin):
    fields = ['id','full_name', 'code', 'department', 'email', 'telephone']
    list_display = ['id','full_name', 'code', 'department', 'email', 'telephone']
    search_fields = ['id','full_name', 'code', 'department', 'email', 'telephone']
    list_filter = ['id','full_name', 'code', 'department', 'email', 'telephone']


class ContractDescAdmin(admin.ModelAdmin):
    fields = ['contract_id', 'contract_number', 'client_name', 'customer_id', 'plate_number', 'other_doc', 'mrc', 'notes']
    list_display = ['contract_id', 'contract_number', 'client_name', 'customer_id', 'plate_number', 'other_doc', 'mrc', 'notes']
    search_fields = ['contract_id', 'contract_number', 'client_name', 'customer_id', 'plate_number', 'other_doc', 'mrc', 'notes']
    list_filter = ['contract_id', 'contract_number', 'client_name', 'customer_id', 'plate_number', 'other_doc', 'mrc', 'notes']


class CustomerAdmin(admin.ModelAdmin):
    fields = ['id', 'name', 'cert_front', 'cert_back', 'contract_deliverer', 'contract_desc']
    list_display =  ['id', 'name', 'cert_front', 'cert_back', 'contract_deliverer', 'contract_desc']
    search_fields = ['id', 'name', 'cert_front', 'cert_back', 'contract_deliverer', 'contract_desc']
    list_filter = ['id', 'name', 'cert_front', 'cert_back', 'contract_deliverer', 'contract_desc']


admin.site.register(CertificationFront, CertificationFrontAdmin)
admin.site.register(CertificationBack, CertificationBackAdmin)
admin.site.register(ContractDeliverer, ContractDelivererAdmin)
admin.site.register(ContractDesc, ContractDescAdmin)
admin.site.register(Customer, CustomerAdmin)