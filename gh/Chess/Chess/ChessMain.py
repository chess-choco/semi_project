import pygame as p
from Chess import ChessBoard

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


# 기물 이미지 파일 불러오기
def load_images():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


# 메인 코드. 입력에 따라 그래픽 움직임
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessBoard.GameState()
    load_images()

    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


# 현 상황에 맞춰 그래픽을 구현
def draw_game_state(screen, gs):
    draw_board(screen)  # 체스판에 격자를 그림
    draw_pieces(screen, gs.board)  # 체스판에 기물을 그림


# 체스판 츨력. 왼쪽 맨 아래 칸은 검은색, 왼쪽 위 칸은 흰색인 것을 기준으로 함
def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            color = colors[((i+j) % 2)]
            p.draw.rect(screen, color, p.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))


# 현재의 GameState.board를 사용하여 기물을 체스판 위에 출력
def draw_pieces(screen, board):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            piece = board[i][j]
            if piece != "--":  # 빈칸이 아니라면
                screen.blit(IMAGES[piece], p.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
