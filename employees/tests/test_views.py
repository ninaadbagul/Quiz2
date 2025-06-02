from django.test import TestCase
from rest_framework.test import APIClient
from employees.models import Employee

class EmployeeViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.emp = Employee.objects.create(
            name="Test Employee",
            department="IT",
            designation="Developer",
            location="Pune",
            date_joined="2023-01-01"
        )

    def test_employee_list(self):
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.data)

    def test_employee_summary(self):
        response = self.client.get(f'/employees/{self.emp.id}/summary/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['employee']['name'], "Test Employee")

    def test_analytics_summary(self):
        response = self.client.get('/analytics/summary/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('total_employees', response.data)
