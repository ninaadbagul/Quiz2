from django.urls import path
from .views import EmployeeListCreateView, EmployeeSummaryView, AnalyticsSummaryView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/summary/', EmployeeSummaryView.as_view(), name='employee-summary'),
    path('analytics/summary/', AnalyticsSummaryView.as_view(), name='analytics-summary'),
]

