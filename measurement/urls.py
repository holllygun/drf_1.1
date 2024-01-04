from django.contrib import admin
from django.urls import path

from measurement import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', views.SensorListView.as_view(), name='create-sensor-list)'),
    path('sensors/<pk>/', views.SensorUpdateView.as_view(), name='detailed-sensor'),
    path('measurements/', views.TemperatureCreateView.as_view(), name='create-measurement'),
]
