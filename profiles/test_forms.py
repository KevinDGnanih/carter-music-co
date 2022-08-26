from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForms(TestCase):

    def test_create_profile_form(self):
        form = UserProfileForm({
            'profile': 'Gia',
            'email': 'gia_gn@gmail.com',
            'phone_number': '062159070',
            'street_adress1': '95 test street',
            'town_or_city': 'test city',
            'country': 'FR'})
        self.assertTrue(form.is_valid())
