from django.db import models

# Create your models here.

class ChessBoard(models.Model):
    # Each chessboard will be uniquely identified by an ID field
    # You can add additional fields as needed
    # For example, if you want to keep track of the current player's turn, you could add a 'current_player' field
    id = models.AutoField(primary_key=True)
    
    # The board state is represented as a string of FEN notation
    # You can read more about FEN notation here: https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
    # This field can be used to store the current state of the board
    board_state = models.CharField(max_length=100)
    
    # You can add additional fields to represent metadata about the board
    # For example, if you want to keep track of whether the game is ongoing or finished, you could add a 'game_status' field
    # And if you want to store the result of the game, you could add a 'result' field


class ChessPiece(models.Model):
    PIECE_CHOICES = (
        ('K', 'King'),
        ('Q', 'Queen'),
        ('R', 'Rook'),
        ('B', 'Bishop'),
        ('N', 'Knight'),
        ('P', 'Pawn')
    )
    color = models.CharField(max_length=1)
    piece_type = models.CharField(max_length=1, choices=PIECE_CHOICES)

class ChessOpening(models.Model):
    name = models.CharField(max_length=200)
    moves = models.TextField()
    eco_code = models.CharField(max_length=10)


class ChessResult(models.Model):
    winner = models.CharField(max_length=1, blank=True, null=True)
    result_type = models.CharField(max_length=10)