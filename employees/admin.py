from django.contrib import admin
from .models import Employee, Attendance, Performance

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'designation', 'location')  # customize fields to show
    search_fields = ('name', 'department')  # searchable fields
    list_filter = ('department', 'designation', 'location')  # filter sidebar

admin.site.register(Employee, EmployeeAdmin)

# Register other models without customization (or add custom admins if you want)
admin.site.register(Attendance)
admin.site.register(Performance)
