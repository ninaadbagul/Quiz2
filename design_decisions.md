## 🧠 Architectural Decisions

### 1. Django + DRF
- Familiar, powerful, and rapid to scaffold during time-boxed challenges.
- DRF provides auto-serialization, throttling, auth, and API documentation support.

### 2. PostgreSQL
- Chosen for reliability and compatibility with Docker.
- Structured model relationships using `ForeignKey` and `OneToOneField`.

### 3. Faker for Data Seeding
- Used to quickly create realistic employee and performance data.
- Seed script integrated as a custom Django management command.

### 4. Docker Setup
- Dockerized to ensure easy deployment, testability, and reproducibility.
- docker-compose manages web + db containers.

### 5. .env Configuration
- Isolated sensitive settings and DB credentials for security.
- Supports multiple environments easily.

### 6. Optional Features Added
| Feature                | Status | Notes |
|------------------------|--------|-------|
| Docker + Compose       | ✅     | Fully working |
| .env config            | ✅     | Done using python-dotenv |
| Health Check           | ✅     | `/health/` endpoint returns 200 |
| Logging                | ✅     | Basic log capture in settings |
| CSV Export             | ✅     | `/employees/export/` implemented |
| Custom Admin UI        | ✅     | Enhanced list display, filters |
| Swagger Documentation  | ✅     | drf-yasg enabled |
| Testing                | ✅     | Added unit test for employee creation |

### 7. Trade-offs Made in 3-Hour Limit
- Frontend charts were minimal (Plotly via templates, could be extended)
- Authentication implemented using token, skipped refresh/blacklist.
- Prioritized clear architecture, visualizations, and REST API clarity over bulk data volume.

### 8. Future Enhancements
- Role-based access
- Frontend UI with React/Vue
- Historical performance trends
- More visual insights
