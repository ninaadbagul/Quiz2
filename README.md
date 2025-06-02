# Employee Analytics API - Quiz 2 (Glynac.ai)

A Django + DRF-based web application that generates synthetic employee data, stores it in PostgreSQL, and provides analytical summaries via REST APIs and visualizations.

---

## 🚀 Features

- ✅ Synthetic employee and performance data generation using Faker
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
- ✅ Custom Django Admin UI

---

## 🏗️ Project Structure

```
employee_project/
├── employees/             # App containing models, serializers, views
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── utils/faker_seed.py
├── employee_project/      # Main project settings
│   ├── settings.py
│   └── urls.py
├── static/                # Plotly charts
├── templates/             # Optional for charts if used
├── Dockerfile
├── docker-compose.yml
├── .env
├── requirements.txt
├── README.md
├── design_decisions.md
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

- /employees/ — List employees (filter + pagination)
- /summary/ — Returns performance analytics
- /employees/export/ — CSV export

Authentication: Token-based (obtain via /api/token/)

---

## ✅ Testing (Optional)
```bash
python manage.py test
```

---

## 👨‍💻 Author
Ninaad Sanjay Bagul

---

## 📄 License
MIT