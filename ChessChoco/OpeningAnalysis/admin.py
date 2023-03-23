from django.contrib import admin
from OpeningAnalysis.models import ChessOpening, ChessVariation, ChessOpeningImage, MoveAnalysis

# Register your models here.

admin.site.register(ChessOpening)
admin.site.register(ChessVariation)
admin.site.register(ChessOpeningImage)
admin.site.register(MoveAnalysis)
