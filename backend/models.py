from django.db import models
from django.conf import settings


import datetime
import pytz
import shortuuid
import numpy as np
import requests
import random
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save, post_save
from mlchain import client

TIMEZONE = pytz.timezone(settings.TIME_ZONE)

def uuid_26():
    return shortuuid.ShortUUID().random(length=26)

def uuid_12(): 
    return shortuuid.ShortUUID().random(length=12)

def uuid_10_number(): 
    return random.randint(0, 9999999999)

def uuid_5(): 
    return shortuuid.ShortUUID().random(length=5)
    
def uuid_hex():
    return uuid.uuid4().hex

class CertificationFront(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    file = models.FileField()

    province_public_security = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Công an tỉnh")
    district_public_security = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text ="Công an huyện")
    number = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=8, help_text="Số giấy chứng nhận")
    
    cre_date = models.DateTimeField(auto_now=True, help_text="Ngày tạo")
    upd_date = models.DateTimeField(auto_now=True, help_text="Ngày cập nhật")

    def save(self, *args, **kwargs): 
        self.upd_date =  datetime.datetime.now(TIMEZONE)
        super(Motorbike_regis_cert, self).save(*args, **kwargs)

    class Meta:
        ordering = ['cre_date']


class CertificationBack(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    file = models.FileField()

    owner = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Tên chủ xe")
    address = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Địa chỉ")

    # motorbike's property
    brand = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Nhãn hiệu")
    model_code = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Số loại")
    engine = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Số máy")
    chassis = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Số khung")
    color = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=20, help_text="Màu")
    activation_scope = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Phạm vi hoạt động")
    plate = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=50, help_text="Biển số đăng ký")
    date_of_expiry = models.DateField(default=uuid_10_number(), blank=False, help_text="Giá trị đến ngày")

    cre_date = models.DateTimeField(auto_now=True, help_text="Ngày tạo")
    upd_date = models.DateTimeField(auto_now=True, help_text="Ngày cập nhật")

    def save(self, *args, **kwargs): 
        self.upd_date =  datetime.datetime.now(TIMEZONE)
        super(Motorbike_regis_cert, self).save(*args, **kwargs)

    class Meta:
        ordering = ['cre_date']


class ContractDeliverer(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    file = models.FileField()

    full_name = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Họ và tên")
    code = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=30, help_text="Code")
    department = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Phòng ban")
    email = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Email")
    telephone = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Điện thoại")
    
    cre_date = models.DateTimeField(auto_now=True, help_text="Ngày tạo")
    upd_date = models.DateTimeField(auto_now=True, help_text="Ngày cập nhật")

    def save(self, *args, **kwargs): 
        self.upd_date =  datetime.datetime.now(TIMEZONE)
        super(ContractDeliverer, self).save(*args, **kwargs)

    class Meta:
        ordering = ['cre_date']


class ContractDesc(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    contract_id = models.ForeignKey(ContractDeliverer, db_column='contract_id', on_delete=models.CASCADE, related_name="desc")
    file = models.FileField()

    contract_number = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Số hợp đồng")
    client_name = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Tên khách hàng")
    customer_id = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Số CMND khách hàng")
    plate_number = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Biển số xe")
    other_doc = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=10, help_text="Chứng từ khác")
    mrc = models.BooleanField(help_text="Chứng từ MRC")
    notes = models.CharField(default=uuid_10_number(), blank=True, null=True, max_length=300, help_text="Ghi chú")
    
    cre_date = models.DateTimeField(auto_now=True)
    upd_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs): 
        self.upd_date =  datetime.datetime.now(TIMEZONE)
        super(Contract_desc, self).save(*args, **kwargs)

    class Meta:
        ordering = ['cre_date']
        

class Customer(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(null=True, max_length=10)

    cert_front = models.OneToOneField(CertificationFront, help_text="Mặt trước chứng nhận đăng kí xe mô tô, gắn máy", on_delete=models.CASCADE, null=True, blank=True)
    cert_back = models.OneToOneField(CertificationBack, help_text="Mặt sau chứng nhận đăng kí xe mô tô, gắn máy", on_delete=models.CASCADE, null=True, blank=True)
    
    contract_deliverer = models.OneToOneField(ContractDeliverer, help_text="Thông tin người giao", on_delete=models.CASCADE)
    contract_desc = models.OneToOneField(ContractDesc, help_text="Mô tả", on_delete=models.CASCADE)

    cre_date = models.DateTimeField(auto_now=True)
    upd_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs): 
        self.upd_date =  datetime.datetime.now(TIMEZONE)
        super(Contract_desc, self).save(*args, **kwargs)

    class Meta:
        ordering = ['cre_date']


@receiver(post_save, sender=CertificationFront)
def process_card_front(sender, instance, created, raw, using, update_fields, **kwargs):
    if created:
        # Create Client 
        model = client("https://s1-ekyc.digital-id.vn").model()

        # Call from the file 
        card_str = instance.file.read()
        nparr = np.fromstring(card_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)

        # Get result 
        output = model.predict_card_and_face_embeddings(img_np)
        import ipdb; ipdb.set_trace()
        # Fill to fields 

        # Save 
        instance.save()
