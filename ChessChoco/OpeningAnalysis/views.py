from django.shortcuts import render
from .models import ChessOpening, ChessVariation, ChessOpeningImage

# Create your views here.
def chess_openings(request):
    openings = ChessOpening.objects.all()
    variations = ChessVariation.objects.all()
    images = ChessOpeningImage.objects.all()

    return render(request, 'chess_opening.html', {'openings': openings, 'variations': variations, 'images': images})
