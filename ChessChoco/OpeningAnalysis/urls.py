# OpeningAnalysis > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.chess_openings),
    path("analysis", views.move_analysis),
]
