from django.db import models
from index.models import Item
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    quantity=models.IntegerField(default=1)
   
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_cart_items(self):
        return self.item.all()

    def get_final_price(self):
        return self.quantity *self.item.price

    def __str__(self):
        return self.item.product_name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(Cart)
    def __str__(self):
        return self.user.username
   
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

    