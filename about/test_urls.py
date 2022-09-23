from django.test import SimpleTestCase
from django.urls import reverse, resolve
from about.views import about


class TestAboutUrls(SimpleTestCase):

    def test_about_url(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)