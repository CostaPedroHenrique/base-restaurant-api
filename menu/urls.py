from django.contrib import admin
from django.urls import path
from .views import GroupAPIView, PlateAPIView

urlpatterns = [
    path('groups/', GroupAPIView.as_view(), name='api_cursos'),
    path('plates/', PlateAPIView.as_view(), name='api_plates'),
]
