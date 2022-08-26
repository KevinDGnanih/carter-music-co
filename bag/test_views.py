from django.test import TestCase
from products.models import Product, Category


class TestCartViews(TestCase):

    def test_view_cart(self):
        categories = Category(name="Category Name")
        categories.save()
        product_detail = Product(name="Test product", price=999.00,
                                 description="Test product description",
                                 image="test.jpg")
        product_detail.save()
        response = self.client.get("/bag/")
        self.assertEqual(response.status_code, 200)
