from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.db.models import Q
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Permission
from wsgiref.util import FileWrapper
import mimetypes, os, re

def home(request):
    items=Item.objects.all()
    return render(request,'home.html',{'items':items})

@permission_required('index.add_item', login_url="restricted/")
def admin_view(request):
    items=Item.objects.all()
    return render(request,'CRUD.html',{'items':items})
def admin_only(request):
    return render(request,'restricted.html')

@permission_required('index.add_item',login_url="restricted/")
def upload_item(request): 
    return render(request,'upload.html')
   

def upload(request):
    image=request.FILES['image']
    product_name=request.POST['product_name']
    category=request.POST['category']
    price=request.POST['price']
    items=Item(image=image, product_name=product_name, category=category, price=price)
    items.save()
    return redirect('/inventory')

def download_image(request, pk):
    img = Item.objects.get(pk=pk)
    wrapper = FileWrapper(img.image) 
    content_type = mimetypes.guess_type(str(img.image))[0]
    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Length'] = os.path.getsize(str(img.image))
    response['Content-Disposition'] = "attachment; filename=%s" % img.image
    return response

def search(request):
    if request.method == "GET":
        src=request.GET['search']
        match=Item.objects.filter(Q(product_name__startswith=src)|Q(category__startswith=src)) 
        if match:
            return render(request,'home.html',{'source':match})
        else:
            return HttpResponse('<h1>No match Found</h1>')

@permission_required('index.delete_item',login_url="restricted/")   
def delete(request, pk):
    items=Item.objects.get(pk=pk)
    items.delete()
    return redirect("/inventory")

@permission_required('index.change_item',login_url="restricted/")
def update_form(request, pk):
    items=Item.objects.get(pk=pk)
    return render(request,'edit.html',{'items':items})

def update(request, pk):
    items=Item.objects.get(pk=pk)
    if request.method=="POST":
        items.image=request.FILES['image']
        items.product_name=request.POST['product_name']
        items.category=request.POST['category']
        items.price=request.POST['price']
        items.save()
        return redirect("/inventory")

    else:
        return HttpResponse("record not updated")


