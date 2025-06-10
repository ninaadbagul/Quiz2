from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse, JsonResponse

# Global views
def homepage(request):
    return HttpResponse("<h1>Welcome to the Employee Analytics API</h1><p>Visit <a href='/swagger/'>Swagger Docs</a> for API usage.</p>")

def health_check(request):
    return JsonResponse({"status": "ok"})

schema_view = get_schema_view(
   openapi.Info(
      title="Employee API",
      default_version='v1',
      description="Employee Attendance and Performance API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', homepage, name='homepage'),                      # http://localhost:8000/
    path('health/', health_check, name='health-check'),       # http://localhost:8000/health/
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),                  # http://localhost:8000/api/...
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
