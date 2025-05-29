from rest_framework import serializers
from .models import Employee, Attendance, Performance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    attendances = AttendanceSerializer(many=True, read_only=True)
    performances = PerformanceSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
