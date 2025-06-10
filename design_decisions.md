## 🧠 Architectural Decisions

### 1. Django + Django REST Framework
- Chosen for its maturity, rapid development cycle, and built-in admin.
- DRF simplifies serialization, filtering, pagination, authentication, and view scaffolding.

### 2. PostgreSQL
- Robust, scalable, and well-supported in Docker environments.
- Used ForeignKey and OneToOneField to maintain normalized model relationships.

### 3. Faker for Data Seeding
- Faker generates synthetic but realistic employee, attendance, and performance data.
- Exposed as a custom Django management command: seed_employees.

### 4. Docker + Docker Compose
- Used to isolate and containerize the application stack (web + db).
- Simplifies deployment across environments.
- .env-based config injects secrets and DB settings securely into containers.

### 5. Token-Based Authentication
- Implemented basic token auth using DRF’s TokenAuthentication.
- Suitable for securing APIs during prototyping and small-team use.

### 6. API Documentation with Swagger
- Integrated using drf-yasg for interactive documentation.
- Available at /swagger/, useful for testers, stakeholders, and devs.

### 7. Logging
- Basic error and usage logging configured in settings.py using Django’s logging framework.
- Useful for debugging and monitoring requests.

### 8. Health Check Endpoint
- Lightweight endpoint at /health/ returns HTTP 200 for readiness probes and monitoring.

### 9. CSV Export
- Implemented /employees/export/ to allow CSV download of employee records.
- Useful for offline analysis and reporting.

### 10. Custom Admin UI
- Enhanced with list_display, list_filter, and search_fields for Employee, Attendance, and Performance models.
- Enables better manual inspection of seeded data.

---

## ✅ Optional Features Summary

| Feature                 | Status | Description |
|-------------------------|--------|-------------|
| Docker + Compose        | ✅     | Fully working multi-container setup |
| .env Configuration      | ✅     | Loaded using python-dotenv |
| Health Check Endpoint   | ✅     | Available at /health/ |
| Swagger Documentation   | ✅     | /swagger/ with drf-yasg |
| CSV Export              | ✅     | /employees/export/ |
| Token Auth              | ✅     | Enabled via DRF |
| Logging                 | ✅     | Configured in settings.py |
| Unit Tests              | ✅     | Tests added for views, models |
| Custom Admin Panel      | ✅     | Admin display, search, filters |
| Data Seeding (Faker)    | ✅     | Custom command `seed_employees` |
| Pagination + Filtering  | ✅     | DRF-backed on /employees/ |

---

## ⏳ Trade-offs in 3-Hour Limit

- Authentication implemented via token; skipped refresh/blacklist mechanisms for speed.
- Minimal frontend visualizations; added backend support with Plotly-ready data and basic templates.
- Prioritized backend structure, data modeling, API correctness, and deployability.
- Skipped async tasks, Celery, and real-time updates due to scope/time constraints.

---

## 🌱 Future Enhancements

- OAuth2/JWT-based auth + permissions
- Role-based access control (RBAC)
- Frontend dashboard using React/Vue
- Historical performance analytics
- Asynchronous background tasks (Celery + Redis)
- Caching layer for analytics APIs
