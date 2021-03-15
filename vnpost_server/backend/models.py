from django.db import models
import datetime
import pytz
from django.conf import settings

TIMEZONE = pytz.timezone(settings.TIME_ZONE)
# Create your models here.
class MotorbikeRegisCert(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    file = models.FileField()

    province_public_security = models.CharField(blank=True, null=True, max_length=300, help_text="Công an tỉnh")
    district_public_security = models.CharField(blank=True, null=True, max_length=300, help_text ="Công an huyện")
    number = models.CharField(blank=True, null=True, max_length=8, help_text="Số giấy chứng nhận")
    owner = models.CharField(blank=True, null=True, max_length=300, help_text="Tên chủ xe")
    address = models.CharField(blank=True, null=True, max_length=300, help_text="Địa chỉ")

    # motorbike's property
    brand = models.CharField(blank=True, null=True, max_length=300, help_text="Nhãn hiệu")
    model_code = models.CharField(blank=True, null=True, max_length=300, help_text="Số loại")
    engine = models.CharField(blank=True, null=True, max_length=300, help_text="Số máy")
    chassis = models.CharField(blank=True, null=True, max_length=300, help_text="Số khung")
    color = models.CharField(blank=True, null=True, max_length=20, help_text="Màu")
    activation_scope = models.CharField(blank=True, null=True, max_length=300, help_text="Phạm vi hoạt động")
    plate = models.CharField(blank=True, null=True, max_length=50, help_text="Biển số đăng ký")
    date_of_expiry = models.DateField(blank=False, help_text="Giá trị đến ngày")

    cre_date = models.DateTimeField(auto_now=True, help_text="Ngày tạo")
    upd_date = models.DateTimeField(auto_now=True, help_text="Ngày cập nhật")

    def save(self, *args, **kwargs): 
        self.upd_date =  datetime.datetime.now(TIMEZONE)
        super(Motorbike_regis_cert, self).save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['owner'])
        ]
        ordering = ['cre_date']
        db_table = "Motorbike_Registration_Certificate"


class ContractDeliverer(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    file = models.FileField()

    full_name = models.CharField(blank=True, null=True, max_length=300, help_text="Họ và tên")
    code = models.CharField(blank=True, null=True, max_length=30, help_text="Code")
    department = models.CharField(blank=True, null=True, max_length=300, help_text="Phòng ban")
    email = models.CharField(blank=True, null=True, max_length=300, help_text="Email")
    telephone = models.CharField(blank=True, null=True, max_length=300, help_text="Điện thoại")
    
    cre_date = models.DateTimeField(auto_now=True, help_text="Ngày tạo")
    upd_date = models.DateTimeField(auto_now=True, help_text="Ngày cập nhật")

    def save(self, *args, **kwargs): 
        self.upd_date =  datetime.datetime.now(TIMEZONE)
        super(ContractDeliverer, self).save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['full_name'])
        ]
        ordering = ['cre_date']
        db_table = "ContractDeliverer"


class ContractDesc(models.Model):
    contract_id = models.ForeignKey(ContractDeliverer, db_column='contract_id', on_delete=models.CASCADE, related_name="desc")
    file = models.FileField()

    contract_number = models.CharField(blank=True, null=True, max_length=300, help_text="Số hợp đồng")
    client_name = models.CharField(blank=True, null=True, max_length=300, help_text="Tên khách hàng")
    customer_id = models.CharField(blank=True, null=True, max_length=300, help_text="Số CMND khách hàng")
    plate_number = models.CharField(blank=True, null=True, max_length=300, help_text="Biển số xe")
    other_doc = models.CharField(blank=True, null=True, max_length=10, help_text="Chứng từ khác")
    mrc = models.BooleanField(help_text="Chứng từ MRC")
    notes = models.CharField(blank=True, null=True, max_length=300, help_text="Ghi chú")
    
    cre_date = models.DateTimeField(auto_now=True)
    upd_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs): 
        self.upd_date =  datetime.datetime.now(TIMEZONE)
        super(Contract_desc, self).save(*args, **kwargs)

    class Meta:
        db_table = "Contract_Description"


class Customer(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(null=True, max_length=10)

    cert = models.OneToOneField(MotorbikeRegisCert, help_text="Chứng nhận đăng kí xe mô tô, gắn máy", on_delete=models.CASCADE)
    contract_deliverer = models.OneToOneField(ContractDeliverer, help_text="Thông tin người giao", on_delete=models.CASCADE)
    contract_desc = models.OneToOneField(ContractDesc, help_text="Mô tả", on_delete=models.CASCADE)

