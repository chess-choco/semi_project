import pygame as p
from Chess import ChessBoard

WIDTH = HEIGHT = 512  # 출력할 체스판 크기
DIMENSION = 8  # 체스판 칸 개수 8칸
SQ_SIZE = HEIGHT // DIMENSION  # 한 칸당 크기
MAX_FPS = 30  # 출력할 때 최대 fps
IMAGES = {}  # 이미지 넣기용 dict


def load_images():  # 기물 이미지 로드
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]  # 이미지 이름
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def print_board(screen):  # 체스판 출력
    colors = [p.Color(255, 206, 158), p.Color(209, 139, 71)]  # 왼쪽 맨 아래가 어두운 칸
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            color = colors[(i+j) % 2]
            p.draw.rect(screen, color, p.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def print_pieces(screen, board):  # 기물 출력
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            piece = board[i][j]
            if piece != "--":  # 빈칸이 아니면:
                screen.blit(IMAGES[piece], p.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def print_game_state(screen, gs):  # 그래픽 구현
    print_board(screen)  # 체스판에 격자를 그림
    print_pieces(screen, gs.board)  # 체스판에 기물을 그림


def main():
    p.init()
    clock = p.time.Clock()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    screen.fill(p.Color("white"))
    gs = ChessBoard.GameState()
    load_images()

    run = True
    while run:
        for i in p.event.get():
            if i.type == p.QUIT:
                run = False

        print_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


if __name__ == "__main__":
    main()
