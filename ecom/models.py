from django.db import models

# Create your models here.
class regimodel(models.Model):
    uname=models.CharField(max_length=20)
    email=models.EmailField()
    phn=models.IntegerField()
    psw=models.CharField(max_length=10)
    def __str__(self):
        return self.uname
class productmodel(models.Model):
    prodname=models.CharField(max_length=50)
    prodid=models.CharField(max_length=10)
    prodprc=models.IntegerField()
    descrpt=models.CharField(max_length=200)
    proimg=models.FileField(upload_to='ecom/static')
    # date=models.DateField(auto_now_add=True)

class productmodel1(models.Model):
    itemname=models.CharField(max_length=50)
    img=models.FileField(upload_to='ecom/static')
    price=models.IntegerField()
    prodid1=models.IntegerField()
    descript=models.CharField(max_length=500)
    def __str__(self):
        return self.itemname


class wishmodel1(models.Model):
    uid=models.IntegerField()
    wishid=models.IntegerField()
    itemname=models.CharField(max_length=50)
    img=models.FileField(upload_to='ecom/static')
    price=models.IntegerField()
    descript=models.CharField(max_length=500)
    prodid1=models.IntegerField()
    def __str__(self):
        return self.itemname
#
class cartmodel(models.Model):
    cid=models.IntegerField()
    cartid=models.IntegerField()
    itemname=models.CharField(max_length=50)
    img=models.FileField(upload_to='ecom/static')
    price=models.IntegerField()
    descript=models.CharField(max_length=500)
    prodid1=models.IntegerField()
    def __str__(self):
        return self.itemname
class paymentmodel(models.Model):
    fname=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=500)
    phn=models.IntegerField()
    zip=models.CharField(max_length=20)
    # bname=models.CharField(max_length=50)
    email=models.EmailField()
    # branme=models.CharField(max_length=100)
    # acname=models.CharField(max_length=50)
    # acno=models.IntegerField()
    # expdte=models.DateField()
    def __str__(self):
        return self.fname
class paymodel(models.Model):
    credit=models.IntegerField()
    cvv=models.IntegerField()
    expdte=models.DateField()

class ofrmodel(models.Model):
    itemname=models.CharField(max_length=50)
    img=models.FileField(upload_to='ecom/static')
    price=models.IntegerField()
    descript=models.CharField(max_length=500)
    prodid1=models.IntegerField()
    def __str__(self):
        return self.itemname

class wishmodel(models.Model):
    uid=models.IntegerField()
    wishid=models.IntegerField()
    itemname=models.CharField(max_length=50)
    img=models.FileField(upload_to='ecom/static')
    price=models.IntegerField()
    descript=models.CharField(max_length=500)
    prodid1=models.IntegerField()
    def __str__(self):
        return self.itemname
class reviewmodel(models.Model):
    cust_name=models.CharField(max_length=50)
    comments=models.CharField(max_length=500)
    imag=models.FileField(upload_to='ecom/static')
    def __str__(self):
        return self.cust_name




