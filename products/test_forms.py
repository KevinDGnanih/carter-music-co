from django.test import TestCase
from .forms import ProductForm


class TestProductForms(TestCase):

    def test_create_product_form_incomplete(self):
        form = ProductForm({
            'sku': 'pp50',
            'name': 'New product',
            'description': 'This is the product I am testing',
            'brand': '',
            'rating': '2',
            'price': 222.34})
        self.assertFalse(form.is_valid())

    def test_create_product_form_complete(self):
        form = ProductForm({
            'category': 'electric',
            'sku': 'pp50',
            'name': 'New product',
            'description': 'This is the product I am testing',
            'price': 222.34,
            'color': 'Cherry',
            'brand': 'Taylor',
            'rating': '3',
            'image_url': 'https://res.cloudinary.com/kdcloud-8710/image/upload/v1663964061/cmco_n2tl4f.png',
            'image': 'image.jpg'})
        self.assertFalse(form.is_valid())
