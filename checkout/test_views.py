from django.test import TestCase


class TestCheckoutViews(TestCase):

    def test_get_checkout_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
