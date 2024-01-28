from django import forms
from.models import *



class regform(forms.Form):
    uname=forms.CharField(max_length=20)
    email=forms.EmailField()
    phn=forms.IntegerField()
    psw=forms.CharField(max_length=20)
    cpsw = forms.CharField(max_length=20)
class logform(forms.Form):
    uname=forms.CharField(max_length=20)
    psw=forms.CharField(max_length=20)
class adminform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
class prodform(forms.Form):
    prodname=forms.CharField(max_length=50)
    prodid=forms.CharField(max_length=10)
    prodprc=forms.IntegerField()
    proimg=forms.FileField()
    descrpt=forms.CharField(max_length=200)
class prodformnew(forms.Form):
    itemname=forms.CharField(max_length=100)
    img=forms.FileField()
    price=forms.IntegerField()
    prodid1=forms.IntegerField()
    descript=forms.CharField(max_length=500)
class payform(forms.Form):
    fname = forms.CharField(max_length=50)
    gender = forms.CharField(max_length=20)
    address = forms.CharField(max_length=500)
    phn = forms.IntegerField()
    zip = forms.CharField(max_length=20)
    # bname=forms.CharField(max_length=50)
    email= forms.EmailField()
    # branme = forms.CharField(max_length=100)
    # acname = forms.CharField(max_length=50)
    # acno = forms.IntegerField()
    # expdte=forms.DateField()
class ofrform(forms.Form):
    itemname=forms.CharField(max_length=50)
    img=forms.FileField()
    price=forms.IntegerField()
    descript = forms.CharField(max_length=500)
    prodid1 = forms.IntegerField()
class review(forms.Form):
    cust_name=forms.CharField(max_length=50)
    comments=forms.CharField(max_length=500)
    imag=forms.FileField()
class payf(forms.Form):
    credit=forms.IntegerField()
    cvv=forms.IntegerField()
    expdte=forms.DateField()


