from django.shortcuts import render
from django.http import HttpResponse
from .models import ChessOpening

# Create your views here.
def index(request):
    return render(request, "opening.html")

def chess_openings(request):
    openings = [
        {'name': 'Sicilian Defense', 'moves': '1.e4 c5'},
        {'name': 'French Defense', 'moves': '1.e4 e6'},
        {'name': 'Caro-Kann Defense', 'moves': '1.e4 c6'},
        {'name': 'Ruy Lopez', 'moves': '1.e4 e5 2.Nf3 Nc6 3.Bb5'},
        {'name': 'Italian Game', 'moves': '1.e4 e5 2.Nf3 Nc6 3.Bc4'},
    ]
    context = {'openings': openings}
    return render(request, 'chess_opening.html', context)
