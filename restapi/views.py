from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from index.models import Item
import json

@csrf_exempt
def get_post_product(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        items = Item.objects.all()
        print("QuerySet objects => ",items)
        list_of_items = list(items.values("product_name","price","category"))
        print("List of Item objects => ",list_of_items)
        dictionary_name = {
        "items":list_of_items
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['product_name'])
        print(python_dictionary_object['price'])
        print(python_dictionary_object['category'])
        Item.objects.create(product_name=python_dictionary_object['product_name'],price=python_dictionary_object['price'],
         category=python_dictionary_object['category'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def get_update_delete(request,Id):
    print("What's the request =>",request.method)
    item = Item.objects.get(id = Id)
    if request.method == "GET":
        print(type(item.product_name))
        return JsonResponse({
            "product_name":item.product_name,
            "price":item.price,
            "category":item.category
        })
    elif request.method=="DELETE":
        item = Item.objects.get(id = id)
        item.delete()
        return JsonResponse({
            "message":"Successfully deleated!!"
        })

    elif request.method == "PUT":
        update = json.loads(request.body)
        item.product_name=update['product_name']
        item.price=update['price']
        item.category=update['category']
        item.save()
        return JsonResponse({
            "message":"Successfully Updated!!"})

    
@csrf_exempt 
def pagination(request,PAGENO,SIZE):
    skip=SIZE*(PAGENO -1)
    item=Item.objects.values() [skip:(PAGENO*SIZE)]
    
    dict={
        "item":list(item.values("product_name","category","price"))
        }
    return JsonResponse(dict)