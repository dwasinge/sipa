from django.urls import path, include
from health.views import health

urlpatterns = [
    path('health/', health),
    path('api/v1/sipa/', include('api.urls')),
]
