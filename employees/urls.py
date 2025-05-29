from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import EmployeeListCreateView, EmployeeSummaryView, AnalyticsSummaryView

schema_view = get_schema_view(
    openapi.Info(
        title="Employee API",
        default_version='v1',
        description="API documentation for Employee project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # List all employees or create a new employee
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),

    # Get summary (details + attendance + performance) for a specific employee by ID
    path('employees/<int:pk>/summary/', EmployeeSummaryView.as_view(), name='employee-summary'),

    # Get analytics summary across all employees and performances
    path('analytics/summary/', AnalyticsSummaryView.as_view(), name='analytics-summary'),

    # Swagger UI for API documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
