from rest_framework import generics, views, filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee, Attendance, Performance
from .serializers import EmployeeSerializer, AttendanceSerializer, PerformanceSerializer
from django.db.models import Avg, Count

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields for exact filtering
    filterset_fields = ['department', 'designation', 'location']

    # Fields for search
    search_fields = ['name', 'department', 'designation', 'location']

    # Fields for ordering
    ordering_fields = ['name', 'date_joined']

class EmployeeSummaryView(views.APIView):
    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)

        attendances = Attendance.objects.filter(employee=employee)
        performances = Performance.objects.filter(employee=employee)

        return Response({
            "employee": EmployeeSerializer(employee).data,
            "attendances": AttendanceSerializer(attendances, many=True).data,
            "performances": PerformanceSerializer(performances, many=True).data
        })

class AnalyticsSummaryView(views.APIView):
    def get(self, request):
        avg_score = Performance.objects.aggregate(avg_score=Avg('score'))['avg_score']
        attendance_count = Attendance.objects.values('status').annotate(count=Count('status'))
        total_employees = Employee.objects.count()

        return Response({
            "average_performance_score": avg_score,
            "attendance_breakdown": attendance_count,
            "total_employees": total_employees
        })
