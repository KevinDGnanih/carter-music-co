from django.test import TestCase
from .models import Product, Category, Brand


class TestProductModel(TestCase):

    def test_string_representation(self):
        product = Product.objects.create(
            name='Test products',
            description='Test description',
            price=199.99
        )
        self.assertEqual(str(product), product.name)

    def test_category_default_to_true(self):
        category = Category.objects.create(name='Electric')
        self.assertTrue(category.name)

    def test_brand_default_to_true(self):
        category = Brand.objects.create(name='Gibson')
        self.assertTrue(category.name)
