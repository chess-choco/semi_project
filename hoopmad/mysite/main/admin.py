from django.contrib import admin
from main.models import ChessPiece, ChessOpening, ChessResult, ChessBoard

admin.site.register(ChessPiece)
admin.site.register(ChessOpening)
admin.site.register(ChessResult)
admin.site.register(ChessBoard)