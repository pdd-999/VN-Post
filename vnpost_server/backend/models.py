from django.db import models

# Create your models here.
class Motorbike_regis_cert(models.Model):
    cert_id = models.CharField(max_length=10, primary_key=True)
    province_public_security = models.CharField(max_length=300)
    district_public_security = models.CharField(max_length=300)
    number = models.CharField(max_length=8)
    owner = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    
    # motorbike's property
    brand = models.CharField(max_length=300)
    model_code = models.CharField(max_length=300)
    engine = models.CharField(max_length=300)
    chassis = models.CharField(max_length=300)
    color = models.CharField(max_length=20)
    activation_scope = models.CharField(max_length=300, blank=True)
    plate = models.CharField(max_length=50)
    date_of_expiry = models.DateField(blank=False)

    cre_date = models.DateTimeField(auto_now=True)
    upd_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs): 
        self.upd_date =  datetime.datetime.now(TIMEZONE)
        super(Motorbike_regis_cert, self).save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['cert_id']),
            models.Index(fields=['owner'])
        ]
        ordering = ['cre_date']
        db_table = "Motorbike_Registration_Certificate"


class Contract_deliverer(models.Model):
    deliverer_id = models.CharField(max_length=10, primary_key=True)
    full_name = models.CharField(max_length=300)
    code = models.CharField(max_length=30)
    department = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    telephone = models.CharField(max_length=300)
    
    cre_date = models.DateTimeField(auto_now=True)
    upd_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs): 
        self.upd_date =  datetime.datetime.now(TIMEZONE)
        super(Motorbike_regis_cert, self).save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['deliverer_id']),
            models.Index(fields=['full_name'])
        ]
        ordering = ['cre_date']
        db_table = "Contract_Deliverer"


class Contract_desc(models.Model):
    deliverer_id = models.ForeignKey(Contract_deliverer, db_column='deliverer_id', on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=300)
    client_name = models.CharField(max_length=300)
    customer_id = models.CharField(max_length=300, blank=True)
    plate_number = models.CharField(max_length=300, blank=True)
    other_doc = models.CharField(max_length=10, blank=True)
    mrc = models.BooleanField()
    notes = models.CharField(max_length=300, blank=True)

    class Meta:
        db_table = "Contract_Description"