
from django.shortcuts import render
from .models import Order, Cart
from index.models import Item
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages

def cart_detail_view(request):
    order = Order.objects.get(user=request.user)
    context = {
        'order':order
    }
    return render(request,'cart.html',context)

def add_item_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect("carts")
        else:
            order.items.add(order_item)
            return redirect("carts")
    else:
        order = Order.objects.create(
            user=request.user)
        order.items.add(order_item)
        return redirect("carts")


def delete_item_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(
        user=request.user)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect(reverse("carts"))
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("carts")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("carts")


def checkout(request):
    return render(request,'thankyou.html')
