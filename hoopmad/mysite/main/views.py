import uuid
from django.shortcuts import render
from .models import ChessBoard

def chess_board(request):
    # Generate a unique chessboard ID
    # chessboard_id = uuid.uuid4().hex
    
    # Create a new Chessboard object with the specified board state
    board_state = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
    chessboard = ChessBoard(board_state=board_state)
    
    # Save the new Chessboard object to the database
    chessboard.save()
    
    # Render the game.html template with the chessboard ID and board state passed in as context
    return render(request, 'main/chess_board.html', {'chessboard_id': chessboard.id, 'board_state': board_state})

def index(request):
    return render(request, "main/index.html")

# def chess_board(request):
#    return render(request, 'main/chess_board.html')