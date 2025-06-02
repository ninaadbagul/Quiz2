from django.test import TestCase
from rest_framework.test import APIClient
from employees.models import Employee

class ExportTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Employee.objects.create(
            name="CSV Export",
            department="HR",
            designation="Recruiter",
            location="Delhi",
            date_joined="2022-01-01"
        )

    def test_export_csv(self):
        response = self.client.get('/employees/export/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/csv', response['Content-Type'])
