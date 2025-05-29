from rest_framework import generics, views
from rest_framework.response import Response
from .models import Employee, Attendance, Performance
from .serializers import EmployeeSerializer, AttendanceSerializer, PerformanceSerializer
from django.db.models import Avg, Count

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

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
