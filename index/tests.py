from django.test import TestCase
from .models import Item
# models test
class Test_product(TestCase):

    def test_product_price(self):
       item =Item.objects.create(price=10)
       self.assertTrue(item.test_price())

    def test_Product_category(self):
        item=Item.objects.create(product_name="jug",category="grocessory",price=10)
        self.assertTrue(item.test_product_category())

    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_contains_correct_templete(self):
        response = self.client.get('/')
        self.assertContains(response, 'home.html')