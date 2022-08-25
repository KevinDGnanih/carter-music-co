from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (
    all_products, add_product, product_detail, edit_product, delete_product)


class TestProductsUrls(SimpleTestCase):

    def test_all_services_urls_resolves(self):
        url = reverse('products')
        self.assertEqual(resolve(url).func, all_products)

    def test_add_url_resolves(self):
        url = reverse('add_product')
        self.assertEqual(resolve(url).func, add_product)

    def test_product_detail_url_resolves(self):
        url = reverse('product_detail', args=('1',))
        self.assertEqual(resolve(url).func, product_detail)

    def test_edit_url_resolves(self):
        url = reverse('edit_product', args=('2',))
        self.assertEqual(resolve(url).func, edit_product)

    def test_delete_url_resolves(self):
        url = reverse('delete_product', args=('3',))
        self.assertEqual(resolve(url).func, delete_product)
