from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
import os
from django.contrib import messages
from django.core.mail import send_mail
# from django.urls import reverse_lazy
# from datetime import date
# import datetime
# from django.views import generic


# Create your views here.
def proj(request):
    return render(request,'front.html')
def first(request):
    return render(request,'first.html')
def about(request):
    return render(request,'about.html')

def regi(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['uname']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phn']
            ps=a.cleaned_data['psw']
            cps=a.cleaned_data['cpsw']
            if ps==cps:
                b=regimodel(uname=un,email=em,phn=ph,psw=ps)
                b.save()
                subject='your account has been created'
                message=f"your homecenter account has been created successfully"
                email_from = 'sreesibin77@gmail.com'
                email_to=em
                send_mail(subject,message,email_from,[email_to])
                return redirect(log)
                # return HttpResponse("successfully registerd")
            else:
                return HttpResponse("password doesnt match")
        else:
            return HttpResponse("failed")

    return render(request,'reg.html')

def log(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['uname']
            ps=a.cleaned_data['psw']
            b=regimodel.objects.all()
            for i in b:
                if i.uname==un and i.psw==ps:
                    request.session['id']=i.id
                    return redirect(userdsp)
                    # return HttpResponse("success")
            else:
                return HttpResponse("failed")
        return HttpResponse("error")

    return render(request,'login.html')
def profile(request):
    id1=request.session['id']
    a=regimodel.objects.get(id=id1)
    return render(request,'profile.html',{'a':a})

def admnlog(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            us=a.cleaned_data['username']
            ps=a.cleaned_data['password']
            b = User.objects.all()
            user = authenticate(request, username=us, password=ps)
            if user is not None:
                return redirect(admnpge)
                # return HttpResponse("success")
            else:
                return HttpResponse("login failed....")
    return render(request,'admnlgn.html')
# def admnupld(request):
#     if request.method=='POST':
#         a=prodform(request.POST,request.FILES)
#         if a.is_valid():
#             pn=a.cleaned_data['prodname']
#             pi=a.cleaned_data['prodid']
#             pp=a.cleaned_data['prodprc']
#             pg=a.cleaned_data['proimg']
#             de=a.cleaned_data['descrpt']
#             # b=productmodel.objects.all()
#             # for i in b:
#             #     if pi == i.productid:
#             #         return HttpResponse("product already uploaded")
#             c=productmodel(prodname=pn,prodid=pi,prodprc=pp,proimg=pg,descrpt=de)
#             c.save()
#             return HttpResponse("successfully uploaded")
#             # return redirect(proddsply)
#         else:
#             return HttpResponse("failed")
#     return render(request,'admnupld.html')
def useredit(request,id):
    a=regimodel.objects.get(id=id)
    if request.method=='POST':
        a.uname=request.POST.get('uname')
        a.email=request.POST.get('email')
        a.phn=request.POST.get('phn')
        a.psw=request.POST.get('psw')
        a.save()
        return redirect(profile)
    return render(request,'edit.html',{'a':a})

def admnupld(request):
    if request.method == "POST":
        a=prodformnew(request.POST,request.FILES)
        if a.is_valid():
            it=a.cleaned_data['itemname']
            im=a.cleaned_data['img']
            pr=a.cleaned_data['price']
            pid=a.cleaned_data['prodid1']
            de=a.cleaned_data['descript']
            c=productmodel1.objects.all()
            for i in c:
                if pid == i.prodid1 :
                    return HttpResponse("already")
            b=productmodel1(itemname=it,img=im,price=pr,prodid1=pid,descript=de)
            b.save()
            # return HttpResponse("Product upload successs")
            return redirect(admndsp)

        else:
            return HttpResponse("failed")
    return render(request,'admnupld1.html')
def admnpge(request):
    return render(request,'admin.html')
def admndsp(request):
    a=productmodel1.objects.all()
    id1=[]
    ite=[]
    im=[]
    pr=[]
    des=[]
    for i in a:
        id=i.id
        id1.append(id)
        it=i.itemname
        ite.append(it)
        ig=str(i.img).split('/')[-1]
        im.append(ig)
        pri=i.price
        pr.append(pri)
        de=i.descript
        des.append(de)
    pair=zip(id1,ite,im,pr,des)
    return render(request,'admndsply.html',{'a':pair})
def userdsp(request):
    a=productmodel1.objects.all()
    id1=[]
    it=[]
    im=[]
    pr=[]
    des=[]
    pi=[]
    for i in a:
        id2 = i.id
        id1.append(id2)
        ite = i.itemname
        it.append(ite)
        ig = str(i.img).split('/')[-1]
        im.append(ig)
        pri = i.price
        pr.append(pri)
        de = i.descript
        des.append(de)
        pri=i.prodid1
        pi.append(pri)
    pair=zip(id1,it,im,pr,des,pi)
    return render(request,'productdisply.html',{'a':pair,})


def uploddelete(request,id):
    a = productmodel1.objects.get(id=id)
    os.remove(str(a.img))
    a.delete()
    return redirect(admndsp)
# #
def uplodedit(request,id):
    a = productmodel1.objects.get(id=id)
    imag = str(a.img).split('/')[-1]
    if request.method == 'POST':
        a.itemname = request.POST.get('itemname')
        a.price = request.POST.get('price')
        a.descript=request.POST.get('descript')
        a.prodid1=request.POST.get('prodid1')
        if request.FILES.get('img') == None:
            a.save()
        else:
            a.img = request.FILES['img']
            a.save()
        a.save()
        return redirect(admndsp)
    return render(request, 'upldedit.html', {'a': a, 'imag': imag})

def sofa(request):
    return render(request,'sofa1.html')

def wishlist(request,id):
    a=productmodel1.objects.get(id=id)
    ig=str(a.img).split('/')[-1]
    wish=wishmodel1.objects.all()
    for i in wish:
        if i.wishid==a.id and i.uid == request.session['id']:
            return HttpResponse("item already")
    b=wishmodel1(itemname=a.itemname,img=ig,price=a.price,descript=a.descript,prodid1=a.prodid1,wishid=a.id,uid=request.session['id'])
    b.save()
    return redirect(wishview)
    # return HttpResponse("addedd to wishlist")


def wishdelete(request,id):
    w=regimodel.objects.get(id=id)
    b=productmodel1.objects.all()
    c=wishmodel1.objects.all()
    for i in c:
        for j in b:
            if j.prodid1==i.prodid1:
                if w.id==i.uid:
                    i.delete()
                    return redirect(wishview)
def wishview(request):
    try:
        id = request.session['id']
        a = wishmodel1.objects.all()
        ui = []
        it = []
        im = []
        pr = []
        des = []
        pi = []
        for i in a:
            id2 = i.uid
            ui.append(id2)
            ite = i.itemname
            it.append(ite)
            ig = str(i.img).split('/')[-1]
            im.append(ig)
            pri = i.price
            pr.append(pri)
            de = i.descript
            des.append(de)
            pri = i.prodid1
            pi.append(pri)
        pair = zip(ui, it, im, pr, des, pi)
        return render(request, 'wshlstdsp.html', {'a': pair, 'id': id})
    except:
        return redirect(regi)




def empty(request):
    a=wishmodel1.objects.all()
    return render(request,'emptylist.html',{'a':a})

def cart(request,id):
    a=productmodel1.objects.get(id=id)
    im=str(a.img).split('/')[-1]
    b=cartmodel.objects.all()
    for i in b:
        if i.cartid==a.prodid1 and i.cid==request.session['id']:
            return HttpResponse("already")
    c=cartmodel(itemname=a.itemname,img=im,price=a.price,descript=a.descript,prodid1=a.prodid1,cartid=a.id,cid=request.session['id'])
    c.save()
    return redirect(cartview)
    # return HttpResponse("item added")

def cartview(request):
    id = request.session['id']
    a=cartmodel.objects.all()
    ci=[]
    it = []
    im = []
    pr = []
    des = []
    pi = []
    # w=0
    total=0
    discount=1099
    amount=0
    for i in a:
        id2 = i.cid
        ci.append(id2)
        ite = i.itemname
        it.append(ite)
        ig = str(i.img).split('/')[-1]
        im.append(ig)
        pri = i.price
        pr.append(pri)
        de = i.descript
        des.append(de)
        pri = i.prodid1
        pi.append(pri)
        W = i.cid
        if W == id:
            total += i.price
        amount = total - discount
    pair = zip(ci, it, im, pr, des, pi)
    return render(request, 'cartdsp.html', {'a': pair, 'total': total, 'amount': amount, "id": id})

def pay1(request):
    if request.method=="POST":
        a=payform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            ge=a.cleaned_data['gender']
            add=a.cleaned_data['address']
            ph=a.cleaned_data['phn']
            zi=a.cleaned_data['zip']
            # bk=a.cleaned_data['bname']
            em=a.cleaned_data['email']
            # br=a.cleaned_data['branme']
            # ac=a.cleaned_data['acname']
            # an=a.cleaned_data['acno']
            # ex=a.cleaned_data['expdte']
            b=paymentmodel(fname=fn,gender=ge,address=add,phn=ph,zip=zi,email=em)
            b.save()
            return redirect(confirmdis1)
            # return HttpResponse('success')
        else:
            return HttpResponse("failed")
    return render(request,'index.html')

def confirmdis(request):
    id1 = request.session['id']
    a=paymentmodel.objects.all()
    return render(request,'index3.html',{'a':a,'id':id1})

def confirmdis1(request):
    a = paymentmodel.objects.all()
    return render(request, 'indx4.html', {'a': a})
def pay(request):
    if request.method=='POST':
        a=payf(request.POST)
        if a.is_valid():
            cre=a.cleaned_data['credit']
            cv=a.cleaned_data['cvv']
            exp=a.cleaned_data['expdte']
            b=paymodel(credit=cre,cvv=cv,expdte=exp)
            b.save()
            return redirect(success)
        else:
            return HttpResponse('failed')
    return render(request,'payment.html')

def success(request):
    a=paymodel.objects.all()
    return render(request,'successurl.html',{'a':a})

# def confirmdis1(request):
#     id1 = request.session['id']
#     a=paymentmodel.objects.all()
#     c=cartmodel.objects.all()
#     fn=[]
#     ph=[]
#     ad=[]
#     bn=[]
#     br=[]
#     zi=[]
#     acn=[]
#     aco=[]
#     for i in a:
#         fna=i.fname
#         fn.append(fna)
#         ph1=i.phn
#         ph.append(ph1)
#         add=i.address
#         ad.append(add)
#         bnk=i.bname
#         bn.append(bnk)
#         bra=i.branme
#         br.append(bra)
#         zi1=i.zip
#         zi.append(zi1)
#         acna=i.acname
#         acn.append(acna)
#         acon=i.acno
#         aco.append(acon)
#     pair=zip(fn,ph,ad,bn,br,zi,acn,aco)
#     return render(request,'indx4.html',{"b":pair,'id':id1})

def ofrupld(request):
    if request.method == "POST":
        a=ofrform(request.POST,request.FILES)
        if a.is_valid():
            it=a.cleaned_data['itemname']
            im=a.cleaned_data['img']
            pr=a.cleaned_data['price']
            pid=a.cleaned_data['prodid1']
            de=a.cleaned_data['descript']
            c=ofrmodel.objects.all()
            for i in c:
                if pid == i.prodid1 :
                    return HttpResponse("already")
            b=ofrmodel(itemname=it,img=im,price=pr,prodid1=pid,descript=de)
            b.save()
            return HttpResponse("successs")
        else:
            return HttpResponse("failed")
    return render(request,'admnupld1.html')
# #dsply
def ofrdsp(request):
    a=ofrmodel.objects.all()
    id1=[]
    it=[]
    im=[]
    pr=[]
    des=[]
    pi=[]
    for i in a:
        id2 = i.id
        id1.append(id2)
        ite = i.itemname
        it.append(ite)
        ig = str(i.img).split('/')[-1]
        im.append(ig)
        pri = i.price
        pr.append(pri)
        de = i.descript
        des.append(de)
        pri=i.prodid1
        pi.append(pri)
    pair=zip(id1,it,im,pr,des,pi)
    return render(request,'ofrdsply.html',{'a':pair,})
def ofrwish(request,id):
    a=ofrmodel.objects.get(id=id)
    ig=str(a.img).split('/')[-1]
    wish=wishmodel.objects.all()
    for i in wish:
        if i.wishid==a.id and i.uid == request.session['id']:
            return HttpResponse("item already")
    b=wishmodel(itemname=a.itemname,img=ig,price=a.price,descript=a.descript,prodid1=a.prodid1,wishid=a.id,uid=request.session['id'])
    b.save()
    return redirect(wishofr)
    # return HttpResponse("addedd to wishlist")
#
# #wsh dsply
def wishofr(request):
    id=request.session['id']
    a=wishmodel.objects.all()
    ui = []
    it = []
    im = []
    pr = []
    des = []
    pi = []
    for i in a:
        id2 = i.uid
        ui.append(id2)
        ite = i.itemname
        it.append(ite)
        ig = str(i.img).split('/')[-1]
        im.append(ig)
        pri = i.price
        pr.append(pri)
        de = i.descript
        des.append(de)
        pri = i.prodid1
        pi.append(pri)
    pair = zip(ui,it, im, pr, des, pi)
    id = request.session['id']
    b = wishmodel1.objects.all()
    ui = []
    it = []
    im = []
    pr = []
    des = []
    pi = []
    for i in b:
        id2 = i.uid
        ui.append(id2)
        ite = i.itemname
        it.append(ite)
        ig = str(i.img).split('/')[-1]
        im.append(ig)
        pri = i.price
        pr.append(pri)
        de = i.descript
        des.append(de)
        pri = i.prodid1
        pi.append(pri)
    pair1 = zip(ui, it, im, pr, des, pi)
    return render(request, 'wshlstdsp.html', {'a': pair,'b':pair1,'id':id, 'id': id})
    # return render(request, 'ofrwshlst.html', {'a': pair,'id':id})
def ofrwshdelete(request,id):
    w=regimodel.objects.get(id=id)
    b=ofrmodel.objects.all()
    c=wishmodel.objects.all()
    for i in c:
        for j in b:
            if j.prodid1==i.prodid1:
                if w.id==i.uid:
                    i.delete()
                    return redirect(wishofr)
# def cart1(request,id):
#     a=ofrmodel.objects.get(id=id)
#     c=productmodel1.objects.get(id=id)
#     im=str(a.img).split('/')[-1]
#     b=cartmodel.objects.all()
#     for i in b:
#         for j in c:
#             if i.cartid==a.id and i.cid==request.session['id']:
#                 if j.prodid1==b.cid and j.id==request.session['id']:
#                     return HttpResponse("already")
#     c=cartmodel(itemname=a.itemname,img=im,price=a.price,descript=a.descript,prodid1=a.prodid1,cartid=a.id,cid=request.session['id'])
#     c.save()
#     return redirect(cartview)
#     # return HttpResponse("item added")
#

def cartdelete(request,id):
    w=regimodel.objects.get(id=id)
    b=productmodel1.objects.all()
    c=cartmodel.objects.all()
    for i in c:
        for j in b:
            if j.prodid1==i.prodid1:
                if w.id==i.cid:
                    i.delete()
                    return redirect(cartview)
def singleview(request,id):
    a=productmodel1.objects.get(id=id)
    im=str(a.img).split('/')[-1]
    return render(request,'singleview.html',{'a':a,'im':im})

def reviewcom(request):
    if request.method=="POST":
        a=review(request.POST,request.FILES)
        if a.is_valid():
            cu=a.cleaned_data['cust_name']
            com=a.cleaned_data['comments']
            im=a.cleaned_data['imag']
            b=reviewmodel(cust_name=cu,comments=com,imag=im)
            b.save()
            return redirect(reviewdsp)
            # return HttpResponse("success")
        else:
            return HttpResponse("failed")
    return render(request,'review1.html')

def reviewdsp(request):
    b = reviewmodel.objects.all()
    cus=[]
    com=[]
    im=[]
    for i in b:
        cu=i.cust_name
        cus.append(cu)
        co=i.comments
        com.append(co)
        imge=str(i.imag).split('/')[-1]
        im.append(imge)
    pair=zip(cus,com,im)
    return render(request, 'front.html', {'b':pair})
def no(request):
    return render(request,'noreview.html')
# def watch(request,id):
#     b = reviewmodel.objects.all()
#     a=productmodel1.objects.get(id=id)
#     id=[]
#     cus = []
#     com = []
#     im = []
#     if b.id == a.id:
#         for i in b:
#             id1=i.id
#             id.append(id1)
#             cu = i.cust_name
#             cus.append(cu)
#             co = i.comments
#             com.append(co)
#             imge = str(i.imag).split('/')[-1]
#             im.append(imge)
#         pair = zip(id,cus, com, im)
#         return render(request, 'noreview.html', {'b': pair, 'a': a})
#     else:
#         return HttpResponse("no review")


def forgot_password(request):
    a=regimodel.objects.all()
    if request.method == 'POST':
        em= request.POST.get('email')
        un= request.POST.get('uname')
        for i in a:
            if(i.email==em and i.uname==un):
                id=i.id
                subject="Password Change"
                message=f"http://127.0.0.1:8000/ecom/change/{id}"
                # message="Renew your password"
                frm="sreesibin77@gmail.com"
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("Check Your E-mail")
        else:
            return HttpResponse("Sorry, Some Error Occured")
    return render(request,'forgot.html')


def change_password(request,id):
    a=regimodel.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('psw')
        p2=request.POST.get('cpsw')
        if p1==p2:
            a.psw=p1
            a.save()
            return redirect(log)
            # return HttpResponse('Password changed')
        else:
            return HttpResponse('Sorry!!')
    return render(request,'change.html')

def logout_view(request):
    logout(request)
    return redirect(first)
