# Employee Analytics API - Quiz 2 (Glynac.ai)

A Django + DRF-based web application that generates synthetic employee data, stores it in PostgreSQL, and provides analytical summaries via REST APIs and visualizations.

---

## 🚀 Features

- ✅ Synthetic employee and performance data generation using Faker
- ✅ Custom Django management command to seed data
- ✅ PostgreSQL database integration
- ✅ REST APIs with pagination, filtering, and throttling (DRF)
- ✅ Swagger UI documentation using drf-yasg
- ✅ Plotly charts for data visualization (optional frontend-ready)
- ✅ Token-based authentication
- ✅ Dockerized deployment with Docker Compose
- ✅ .env-based configuration
- ✅ Health check endpoint
- ✅ Logging of API usage/errors
- ✅ CSV export for employee data
- ✅ Custom Django Admin UI with filters, search, and display

---

## 🏗️ Project Structure

```
employee_project/
├── employees/
│ ├── admin.py # Customized admin interface
│ ├── apps.py
│ ├── models.py # Employee, Attendance, Performance models
│ ├── serializers.py # DRF serializers
│ ├── tests/ # Unit tests
│ │ ├── test_models.py
│ │ ├── test_views.py
│ │ ├── test_auth.py
│ │ ├── test_swagger.py
│ │ └── test_export.py
│ ├── urls.py # App-level URL patterns
│ ├── views.py # Core API logic
│ └── utils/
│ └── faker_seed.py # Custom seeder script
├── employee_project/
│ ├── init.py
│ ├── settings.py # Environment-based config
│ ├── urls.py # Project-level routing
│ └── wsgi.py
├── static/ # Plotly chart files (optional)
├── templates/ # HTML template directory (optional)
├── Dockerfile
├── docker-compose.yml
├── .env # Local dev environment config
├── requirements.txt
├── README.md
├── design_decisions.md # Architectural decisions
└── manage.py
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/ninaadbagul/Quiz2.git
cd Quiz2
```

### 2. Setup Environment Variables
Create a `.env` file:
```
SECRET_KEY=your_django_secret
DEBUG=True
POSTGRES_DB=quiz2db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
DB_HOST=db
```

### 3. Build and Run with Docker
```bash
docker-compose up --build
```

### 4. Apply Migrations and Seed Data
```bash
docker exec -it quiz2-web bash
python manage.py migrate
python manage.py seed_employees  # Custom command to generate fake data
python manage.py createsuperuser
```

### 5. Access
- Swagger UI: http://localhost:8000/swagger/
- Admin Panel: http://localhost:8000/admin/
- Health Check: http://localhost:8000/health/
- CSV Export: http://localhost:8000/employees/export/

---

## 📦 API Highlights

- GET /employees/ — List employees (pagination + search + filter)
- POST /employees/ — Add a new employee
- GET /employees/<id>/summary/ — Employee-wise performance & attendance
- GET /analytics/summary/ — Org-wide performance & attendance analytics 
- GET /employees/export/ — Download employee data as CSV 
- GET /health/ — Health check endpoint 
- GET /swagger/ — Swagger API docs

Authentication: Token-based (obtain via /api/token/)

---

## ✅ Testing

- Run all unit tests:
```bash
python manage.py test
```
- To reseed fake employee data (optional):
```bash
python manage.py seed_employees
```

---

## 👨‍💻 Author
## Ninaad Sanjay Bagul

---

## 📄 License
MIT