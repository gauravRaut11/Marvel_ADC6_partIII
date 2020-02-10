from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cart/<int:id>/', views.add_item_to_cart, name='cart'),
    path('show_cart/',views.cart_detail_view, name = 'carts'),
    path('show_cart/delete/<int:id>/',views.delete_item_from_cart, name='delete_item'),
    path('show_cart/checkout',views.checkout, name = 'checkout'),

]