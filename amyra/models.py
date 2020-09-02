from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    mobile_no = models.BigIntegerField()
    city = models.CharField(max_length=12)
    state = models.CharField(max_length=15)
    gst_no = models.CharField(max_length=20)

    def __str__(self):
        return self.user.get_full_name()


class Destination(models.Model):
    slug = models.SlugField(null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    bill_type = models.CharField(max_length=500, null=True)
    invoice_no = models.CharField(max_length=500, null=True)
    hsn_code = models.CharField(max_length=4)
    dated = models.DateField()
    transport = models.CharField(max_length=500, null=True)
    vehicle_no = models.CharField(max_length=500, null=True)
    challan_no = models.CharField(max_length=500, null=True)
    date = models.DateField()
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    transport_cost = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title


class Calculation(models.Model):
    destination = models.OneToOneField(Destination, on_delete=models.CASCADE)
    total_amount = models.IntegerField(null=True, blank=True)
    sgst = models.IntegerField(null=True, blank=True)
    cgst = models.IntegerField(null=True, blank=True)
    igst = models.IntegerField(null=True, blank=True)
    total_amount_after_tax = models.IntegerField(null=True, blank=True)
    total_amount_in_words = models.CharField(max_length=500, null=True, blank=True, default='')


DIBBI_CHOICE = (
    (6, '6 dibbi'),
    (12, '12 dibbi')
)


class Item(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True)
    sr_no = models.IntegerField()
    design_name = models.CharField(max_length=500)
    qty = models.IntegerField()
    dibbi = models.IntegerField(choices=DIBBI_CHOICE, default=12)
    pics = models.IntegerField(null=True, blank=True, editable=False)
    rate = models.IntegerField()
    amount = models.IntegerField(null=True, blank=True, editable=False)

    def __str__(self):
        return str(self.sr_no)

