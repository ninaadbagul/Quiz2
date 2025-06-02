from django.test import TestCase
from rest_framework.test import APIClient

class AuthTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_admin_login_redirect(self):
        response = self.client.get('/admin/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Log in", str(response.content))
