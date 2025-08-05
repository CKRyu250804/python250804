import pygame
import sys
import random

# 초기화
pygame.init()
WIDTH, HEIGHT = 600, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록깨기 게임")
CLOCK = pygame.time.Clock()

# 한글 폰트 설정 (윈도우 기본 폰트 사용)
try:
    FONT = pygame.font.SysFont("malgungothic", 30)
except:
    FONT = pygame.font.SysFont("Arial", 30)

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 블록 설정
BLOCK_ROWS = 6
BLOCK_COLS = 10
BLOCK_WIDTH = WIDTH // BLOCK_COLS
BLOCK_HEIGHT = 30

# 패들 설정
PADDLE_WIDTH = 100  # 기존 100에서 3배로 증가
PADDLE_HEIGHT = 15
PADDLE_SPEED = 8

# 공 설정
BALL_RADIUS = 10
BALL_SPEED = 6

class Block(pygame.Rect):
    def __init__(self, x, y, color):
        super().__init__(x, y, BLOCK_WIDTH-2, BLOCK_HEIGHT-2)
        self.color = color

def create_blocks():
    blocks = []
    colors = [RED, GREEN, BLUE]
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLS):
            x = col * BLOCK_WIDTH + 1
            y = row * BLOCK_HEIGHT + 1 + 50
            color = colors[row % len(colors)]
            blocks.append(Block(x, y, color))
    return blocks

def draw_blocks(blocks):
    for block in blocks:
        pygame.draw.rect(SCREEN, block.color, block)

def main():
    # 패들
    paddle = pygame.Rect(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
    # 공
    ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS*2, BALL_RADIUS*2)
    ball_dx = BALL_SPEED * random.choice([-1, 1])
    ball_dy = -BALL_SPEED
    # 블록
    blocks = create_blocks()
    score = 0
    running = True
    game_over = False

    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += PADDLE_SPEED

        if not game_over:
            # 공 이동
            ball.x += ball_dx
            ball.y += ball_dy

            # 벽 충돌
            if ball.left <= 0 or ball.right >= WIDTH:
                ball_dx *= -1
            if ball.top <= 0:
                ball_dy *= -1

            # 패들 충돌
            if ball.colliderect(paddle):
                ball_dy *= -1
                ball.y = paddle.y - BALL_RADIUS*2

            # 블록 충돌
            hit_index = ball.collidelist(blocks)
            if hit_index != -1:
                hit_block = blocks.pop(hit_index)
                score += 10
                ball_dy *= -1

            # 바닥에 닿으면 게임 오버
            if ball.bottom >= HEIGHT:
                game_over = True

            # 승리 조건
            if not blocks:
                game_over = True

        draw_blocks(blocks)
        pygame.draw.rect(SCREEN, WHITE, paddle)
        pygame.draw.ellipse(SCREEN, BLUE, ball)
        score_text = FONT.render(f"점수: {score}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))

        if game_over:
            msg = "게임 오버!" if ball.bottom >= HEIGHT else "클리어!"
            over_text = FONT.render(msg, True, RED)
            SCREEN.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2))
            restart_text = FONT.render("R키로 재시작", True, WHITE)
            SCREEN.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 40))
            if keys[pygame.K_r]:
                # 재시작
                paddle.x = WIDTH//2 - PADDLE_WIDTH//2
                ball.x, ball.y = WIDTH//2, HEIGHT//2
                ball_dx = BALL_SPEED * random.choice([-1, 1])
                ball_dy = -BALL_SPEED
                blocks = create_blocks()
                score = 0
                game_over = False

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()