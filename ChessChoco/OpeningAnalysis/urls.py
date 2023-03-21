# OpeningAnalysis > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.chess_openings),
    #path("chess_opening", views.chess_openings),
]
