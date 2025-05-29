import os
import sys
import django
import random
from faker import Faker

# Add the parent directory of 'employee_project' to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_project.settings')
django.setup()

from employees.models import Employee, Attendance, Performance

fake = Faker()
NUM_RECORDS = 5

print("🌱 Starting populate_data script...\n")

def populate_employees(n=NUM_RECORDS):
    print(f"📌 Creating {n} Employee records...")
    for i in range(n):
        try:
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),  # ✅ Ensure uniqueness
                phone=fake.phone_number(),
                designation=fake.job(),
                department=fake.job(),
                date_joined=fake.date_between(start_date='-3y', end_date='today'),
                location=fake.city()
            )
            print(f"✅ [{i+1}/{n}] Created Employee: {employee.name} (ID: {employee.id})")
        except Exception as e:
            print(f"❌ Error creating employee #{i+1}: {e}")
    print("✅ Finished creating employees.\n")

def populate_attendance(n=NUM_RECORDS):
    employees = list(Employee.objects.all())
    if not employees:
        print("⚠️ No employees found. Please create employees first.")
        return

    print(f"📌 Creating {n} Attendance records...")
    for i in range(n):
        try:
            attendance = Attendance.objects.create(
                employee=random.choice(employees),
                date=fake.date_between(start_date='-1y', end_date='today'),
                status=random.choice(['Present', 'Absent', 'Leave']),
            )
            print(f"✅ [{i+1}/{n}] Attendance for Employee ID: {attendance.employee.id} on {attendance.date}")
        except Exception as e:
            print(f"❌ Error creating attendance #{i+1}: {e}")
    print("✅ Finished creating attendance records.\n")

def populate_performance(n=NUM_RECORDS):
    employees = list(Employee.objects.all())
    if not employees:
        print("⚠️ No employees found. Please create employees first.")
        return

    print(f"📌 Creating {n} Performance records...")
    for i in range(n):
        try:
            performance = Performance.objects.create(
                employee=random.choice(employees),
                review_date=fake.date_between(start_date='-1y', end_date='today'),
                score=random.randint(1, 5),
                comments=fake.text(max_nb_chars=200),
            )
            print(f"✅ [{i+1}/{n}] Performance score {performance.score} for Employee ID: {performance.employee.id}")
        except Exception as e:
            print(f"❌ Error creating performance #{i+1}: {e}")
    print("✅ Finished creating performance records.\n")

if __name__ == '__main__':
    try:
        populate_employees()
        populate_attendance()
        populate_performance()
        print("🎉 Fake data population complete.")
    except Exception as main_e:
        print(f"🚨 An error occurred during population: {main_e}")
