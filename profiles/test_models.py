from django.test import TestCase
from .models import UserProfile, User


class TestProfilesModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username',
                                        password='password1234!')

    def test_profile_default(self):
        profile = UserProfile(user=self.user,
                              default_phone_number='Test Phone Number',
                              default_street_address1='Test Address1',
                              default_street_address2='Test Address2',
                              default_town_or_city='Test City',
                              default_county='Test County',
                              default_postcode='Test Postcode',
                              default_country='Test Country')

        self.assertEqual(profile.default_phone_number, 'Test Phone Number')
        self.assertEqual(profile.default_street_address1, 'Test Address1')
        self.assertEqual(profile.default_street_address2, 'Test Address2')
        self.assertEqual(profile.default_town_or_city, 'Test City')
        self.assertEqual(profile.default_county, 'Test County')
        self.assertEqual(profile.default_postcode, 'Test Postcode')
        self.assertEqual(profile.default_country, 'Test Country')

        self.assertEqual("username", str(profile))
