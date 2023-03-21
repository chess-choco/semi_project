from django.shortcuts import render
from django.http import HttpResponse
from .models import ChessOpening

# Create your views here.
def index(request):
    return render(request, "opening.html")

def chess_openings(request):
    openings = ChessOpening.objects.all()
    return render(request, 'chess_opening.html', {'openings': openings})
