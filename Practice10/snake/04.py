import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with Obstacles")

CELL = 30

font = pygame.font.SysFont("Arial", 30)

score = 0
level = 1

# Загрузка картинки Game Over
game_over_image = pygame.image.load("gameover.png")
game_over_image = pygame.transform.scale(
    game_over_image,
    (WIDTH, HEIGHT)
)

# ---------------- GRID ----------------

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(
                screen,
                colorGRAY,
                (i * CELL, j * CELL, CELL, CELL),
                1
            )


def draw_score():
    text = font.render(
        f"Score: {score}   Level: {level}",
        True,
        colorWHITE
    )
    screen.blit(text, (10, 10))

# ---------------- GAME OVER ----------------

def game_over_screen():

    screen.blit(game_over_image, (0, 0))

    text = font.render(
        f"Score: {score}",
        True,
        colorWHITE
    )

    screen.blit(
        text,
        (WIDTH // 2 - 60, 20)
    )

    pygame.display.flip()

    pygame.time.delay(3000)

# ---------------- POINT ----------------

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# ---------------- OBSTACLES ----------------

class Obstacle:

    def __init__(self):

        self.positions = []

        # один фиксированный цвет
        self.color = colorORANGE

        self.generate()

    def generate(self):

        self.positions = []

        for i in range(10):   # количество стен

            x = random.randint(
                0,
                WIDTH // CELL - 1
            )

            y = random.randint(
                0,
                HEIGHT // CELL - 1
            )

            self.positions.append(
                Point(x, y)
            )

    def draw(self):

        for pos in self.positions:

            pygame.draw.rect(
                screen,
                self.color,   # всегда оранжевый
                (
                    pos.x * CELL,
                    pos.y * CELL,
                    CELL,
                    CELL
                )
            )

# ---------------- SNAKE ----------------

class Snake:

    def __init__(self):

        self.body = [
            Point(10, 11),
            Point(10, 12),
            Point(10, 13)
        ]

        self.dx = 1
        self.dy = 0

    def move(self):

        for i in range(
            len(self.body) - 1,
            0,
            -1
        ):

            self.body[i].x = \
                self.body[i - 1].x

            self.body[i].y = \
                self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    # --- СТОЛКНОВЕНИЕ СО СТЕНОЙ

    def check_wall_collision(self):

        head = self.body[0]

        if head.x < 0:
            return True

        if head.x >= WIDTH // CELL:
            return True

        if head.y < 0:
            return True

        if head.y >= HEIGHT // CELL:
            return True

        return False

    # --- СТОЛКНОВЕНИЕ С ПРЕПЯТСТВИЯМИ

    def check_obstacle_collision(
        self,
        obstacles
    ):

        head = self.body[0]

        for pos in obstacles.positions:

            if head.x == pos.x and \
               head.y == pos.y:

                return True

        return False

    def draw(self):

        head = self.body[0]

        pygame.draw.rect(
            screen,
            colorRED,
            (
                head.x * CELL,
                head.y * CELL,
                CELL,
                CELL
            )
        )

        for segment in self.body[1:]:

            pygame.draw.rect(
                screen,
                colorYELLOW,
                (
                    segment.x * CELL,
                    segment.y * CELL,
                    CELL,
                    CELL
                )
            )

    def check_food_collision(self, food):
        global score, level, FPS

        head = self.body[0]

        if head.x == food.pos.x and head.y == food.pos.y:

            score += 1

            self.body.append(Point(head.x, head.y))

            food.generate_random_pos()

    # каждые 3 еды → новый уровень
            if score % 3 == 0:
                level += 1
                FPS += 2   # ускорение

# ---------------- FOOD ----------------

class Food:

    def __init__(self):

        self.pos = Point(9, 9)

    def draw(self):

        pygame.draw.rect(
            screen,
            colorGREEN,
            (
                self.pos.x * CELL,
                self.pos.y * CELL,
                CELL,
                CELL
            )
        )

    def generate_random_pos(self):

        self.pos.x = random.randint(
            0,
            WIDTH // CELL - 1
        )

        self.pos.y = random.randint(
            0,
            HEIGHT // CELL - 1
        )

# ---------------- GAME ----------------

FPS = 5

clock = pygame.time.Clock()

food = Food()
snake = Snake()
obstacles = Obstacle()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0

            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0

            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1

            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    screen.fill(colorBLACK)

    draw_grid()

    snake.move()

    # --- ПРОВЕРКИ ПРОИГРЫША

    if snake.check_wall_collision():

        game_over_screen()
        running = False

    if snake.check_obstacle_collision(
        obstacles
    ):

        game_over_screen()
        running = False

    snake.check_food_collision(food)

    snake.draw()
    food.draw()
    obstacles.draw()
    

    draw_score()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()