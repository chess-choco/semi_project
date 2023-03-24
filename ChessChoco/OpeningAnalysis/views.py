from django.shortcuts import render
from .models import ChessOpening, ChessVariation, ChessOpeningImage, MoveAnalysis

# Create your views here.
def chess_openings(request):
    openings = ChessOpening.objects.all()
    variations = ChessVariation.objects.all()
    images = ChessOpeningImage.objects.all()

    return render(request, 'chess_opening.html', {'openings': openings, 'variations': variations, 'images': images})

def move_analysis(request):
    analysis = MoveAnalysis.objects.all()
    images = MoveAnalysis.objects.all()

    return render(request, 'move_analysis.html', {'analysis': analysis, 'images': images})
