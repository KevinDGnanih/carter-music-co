from django.test import TestCase
from .forms import OrderForm


class TestCheckoutOrderForm(TestCase):

    def test_generate_order_with_required_fields(self):
        form = OrderForm({
            'full_name': 'Gia Gn',
            'email': 'gia_gn@gmail.com',
            'phone_number': '06215970',
            'street_adress1': '24 test street',
            'postcode': '95190',
            'town_or_city': 'test city',
            'country': 'FR'})
        self.assertFalse(form.is_valid())

    def test_generate_message_for_empty_form(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'],
                         ['This field is required.'])
