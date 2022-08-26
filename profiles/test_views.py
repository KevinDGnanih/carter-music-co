from django.test import TestCase


class TestProfilesViews(TestCase):

    def test_get_profile_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
