from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import profile, order_history


class TestProfilesUrls(SimpleTestCase):

    def test_profile_url(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def test_order_history_url(self):
        url = reverse('order_history', args=['some-number'])
        self.assertEqual(resolve(url).func, order_history)
