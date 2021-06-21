from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey
from django.core.validators import RegexValidator

# Create your models here.



class DesignerModel(models.Model):
    alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only Alphabets Are Allowed.')
    phone = RegexValidator(r'^[0-9]{10}$', 'Enter Valid Mobile Number')
    dname =models.CharField(max_length= 100, validators=[alpha])
    dph_no =models.CharField(max_length=10,validators=[phone])
    daddress=models.CharField(max_length=400)

    def __str__(self):
        return self.dname

class CustomerModel(models.Model):
    TYPE =(
        ('Retail Customer','Retail Customer'),
        ('Full Kitchen Customer','Full Kitchen Customer'),
    )
    alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only Alphabets Are Allowed.')
    phone = RegexValidator(r'^[0-9]{10}$', 'Enter Valid Mobile Number')
    fname = models.CharField(max_length=30, validators=[alpha] )
    mname = models.CharField(max_length=30,null =True ,blank=True,validators=[alpha] )
    lname = models.CharField(max_length=30,null =True,blank=True,validators=[alpha] )
    ph_no=models.CharField(max_length=10,null=True,blank=True,validators=[phone])
    address=models.CharField(max_length=400,null =True,blank=True)
    walk_in_date=models.DateField(null =True,blank=True)
    customer_type=models.CharField(max_length=100,null =True,choices=TYPE)
    designer_name=ForeignKey(DesignerModel, on_delete=models.CASCADE,null=True,blank=True)
    visit_date =models.DateField(null =True,blank=True)
    measure_date=models.DateField(null =True,blank=True)
    login_date=models.DateField(null =True,blank=True)
    dispatch_date=models.DateField(null =True,blank=True)
    install_date=models.DateField(null =True,blank=True)

    def __str__(self):
        return self.fname

class productCategoryModel(models.Model):
    alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only Alphabets Are Allowed.')
    name = models.CharField(max_length=30, primary_key=True ,validators=[alpha])
    hsn = models.CharField(max_length=30)
    gst = models.FloatField()

    def __str__(self):
        return self.name

class productModel(models.Model):
    alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only Alphabets Are Allowed.')
    category = ForeignKey(productCategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30 ,validators=[alpha])
    dealersPrice = models.FloatField()
    mrp = models.FloatField()

    def __str__(self):
        return self.name


class accessoriesCategoryModel(models.Model):
    alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only Alphabets Are Allowed.')
    name = models.CharField(max_length=30, primary_key=True,validators=[alpha])
    hsn = models.CharField(max_length=30)
    gst = models.FloatField()

    def __str__(self):
        return self.name

class accessoriesModel(models.Model):
    category = ForeignKey(accessoriesCategoryModel, on_delete=models.CASCADE)
    code = models.CharField(max_length=30)
    dealersPrice = models.FloatField()
    mrp = models.FloatField()
    stdPack = models.IntegerField()
    dimensions = models.CharField(max_length=20)

    def __str__(self):
        return self.code
        
class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel , on_delete= models.CASCADE)
    product = models.ForeignKey(productModel, on_delete= models.CASCADE,null=True,blank=True)
    accessories = models.ForeignKey(accessoriesModel, on_delete= models.CASCADE,null=True,blank=True)

class InvoiceModel(models.Model):
    order_no = models.ForeignKey(OrderModel,on_delete=models.CASCADE)
    totalamount = models.FloatField()

class PaymentModel(models.Model):
    invoice_no = models.ForeignKey(OrderModel,on_delete=models.CASCADE)

class InstallModel(models.Model):
    MODE =(
        ('Cheque','Cheque'),
        ('Cash','Cash'),
        ('Net Banking','Net Banking')
    )
    payid =models.ForeignKey(CustomerModel,on_delete=CASCADE)
    date=models.DateField()
    mode_of_pay = models.CharField(max_length= 60, choices=MODE,null=True,blank=True)
    chequeno = models.CharField(max_length=30,null=True,blank=True)
    amount_paid = models.FloatField()
