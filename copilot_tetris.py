import pygame
import random

# 게임 설정
WINDOW_WIDTH, WINDOW_HEIGHT = 300, 600
BLOCK_SIZE = 30
BOARD_WIDTH, BOARD_HEIGHT = WINDOW_WIDTH // BLOCK_SIZE, WINDOW_HEIGHT // BLOCK_SIZE

# 색상 정의
COLORS = [
    (0, 0, 0),      # 빈칸
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (255, 0, 0),    # Z
    (128, 0, 128),  # T
]

# 테트리스 블록 모양
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[2, 0, 0], [2, 2, 2]],  # J
    [[0, 0, 3], [3, 3, 3]],  # L
    [[4, 4], [4, 4]],        # O
    [[0, 5, 5], [5, 5, 0]],  # S
    [[6, 6, 0], [0, 6, 6]],  # Z
    [[0, 7, 0], [7, 7, 7]],  # T
]

class Tetromino:
    def __init__(self):
        self.type = random.randint(0, len(SHAPES) - 1)
        self.shape = SHAPES[self.type]
        self.x = BOARD_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def create_board():
    return [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def check_collision(board, tetromino, dx=0, dy=0, rotated_shape=None):
    shape = rotated_shape if rotated_shape else tetromino.shape
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                nx, ny = tetromino.x + x + dx, tetromino.y + y + dy
                if nx < 0 or nx >= BOARD_WIDTH or ny >= BOARD_HEIGHT:
                    return True
                if ny >= 0 and board[ny][nx]:
                    return True
    return False

def merge_board(board, tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                board[tetromino.y + y][tetromino.x + x] = cell

def clear_lines(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    lines_cleared = BOARD_HEIGHT - len(new_board)
    for _ in range(lines_cleared):
        new_board.insert(0, [0 for _ in range(BOARD_WIDTH)])
    return new_board, lines_cleared

def draw_board(screen, board, tetromino):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            color = COLORS[board[y][x]]
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    # 현재 블록 그리기
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                px = (tetromino.x + x) * BLOCK_SIZE
                py = (tetromino.y + y) * BLOCK_SIZE
                pygame.draw.rect(screen, COLORS[cell], (px, py, BLOCK_SIZE, BLOCK_SIZE), 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    board = create_board()
    tetromino = Tetromino()
    fall_time = 0
    fall_speed = 500
    score = 0
    running = True

    while running:
        dt = clock.tick()
        fall_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(board, tetromino, dx=-1):
                        tetromino.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(board, tetromino, dx=1):
                        tetromino.x += 1
                elif event.key == pygame.K_DOWN:
                    if not check_collision(board, tetromino, dy=1):
                        tetromino.y += 1
                elif event.key == pygame.K_UP:
                    rotated = [list(row) for row in zip(*tetromino.shape[::-1])]
                    if not check_collision(board, tetromino, rotated_shape=rotated):
                        tetromino.shape = rotated

        if fall_time > fall_speed:
            fall_time = 0
            if not check_collision(board, tetromino, dy=1):
                tetromino.y += 1
            else:
                merge_board(board, tetromino)
                board, lines = clear_lines(board)
                score += lines * 100
                tetromino = Tetromino()
                if check_collision(board, tetromino):
                    running = False  # 게임 오버

        screen.fill((0, 0, 0))
        draw_board(screen, board, tetromino)
        pygame.display.flip()

    print("Game Over! Score:", score)
    pygame.quit()

if __name__ == "__main__":
    main()