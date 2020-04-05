# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from math import ceil
from django.shortcuts import render
from.models import Product,Contact,Orders,Update
# Create your views here.
from django.http import HttpResponse
import json

def index(request):
    allprod = []
    catprods = Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = int(n//4 + ceil((n/4)-(n//4)))
        allprod.append([prod,range(1,nslides),nslides])
    
    params = {'allprods':allprod}
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == 'POST':
        print(request)
        name=request.POST.get('name','')
        print(name)
        email=request.POST.get('email','')
        mob=request.POST.get('mob','')
        desc=request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=mob,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method == 'POST':
        print(request)
        orderid = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            order=Orders.objects.filter(order_id=orderid,email=email)
            if len(order)>0:
                update=Update.objects.filter(order_id=orderid)
                updates=[]
                for item in update:
                   updates.append({'text':item.update_desc,'time': item.timestamp})
                   response = json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)

            else:
                return HttpResponse("Error")
        except Exception as e:
            return HttpResponse("Error")
    return render(request, 'shop/tracker.html')
def search(request):
    return HttpResponse("We are at search")

def productView(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodview.html')

def checkout(request):
    if request.method == 'POST':
        print(request)
        items_json = request.POST.get('itemsjson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')+" "+request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        mob = request.POST.get('phone', '')
        order = Orders(items_json=items_json,name=name, email=email, address=address, city=city,state=state,zip_code=zip_code, phone=mob)
        order.save()
        update=Update(order_id=order.order_id,update_desc="The order has been placed")
        #Name = order.name
        #,update_desc="The order has been placed"
        update.save()
        thank = True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')
