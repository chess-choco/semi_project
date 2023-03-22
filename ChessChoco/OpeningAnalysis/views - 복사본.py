from django.shortcuts import render
from django.http import HttpResponse
from .models import ChessOpening, ChessVariation, ChessOpeningImage

# Create your views here.
def index(request):
    return render(request, "opening.html")

def chess_openings(request):
    openings = ChessOpening.objects.all()
    variations = ChessVariation.objects.all()
    images = ChessOpeningImage.objects.all()

    # Iterate over the openings and print the number of variations for each opening
    for opening in openings:
        num_variations = opening.num_variations()
        print(f"The number of variations for {opening.name} is {num_variations}.")

    return render(request, 'chess_opening.html', {'openings': openings, 'variations': variations, 'images': images})