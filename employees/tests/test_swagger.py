from django.test import TestCase
from rest_framework.test import APIClient

class SwaggerUITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_swagger_ui_loads(self):
        response = self.client.get('/swagger/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Swagger UI', response.content)
