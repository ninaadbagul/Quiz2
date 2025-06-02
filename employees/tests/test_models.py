from django.test import TestCase
from employees.models import Employee

class EmployeeModelTest(TestCase):
    def test_create_employee(self):
        emp = Employee.objects.create(
            name="Test Employee",
            department="Engineering",
            designation="Developer",
            location="Mumbai",
            date_joined="2023-01-01"
        )
        self.assertEqual(str(emp.name), "Test Employee")
