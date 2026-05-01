import pygame
import math
import datetime

# Инициализация pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 900, 500

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Высота панели инструментов
toolbar_height = 120

# Создание окна (с учётом панели снизу)
screen = pygame.display.set_mode((WIDTH, HEIGHT + toolbar_height))
pygame.display.set_caption("Paint TSIS 2 - Fixed")

# Холст для рисования
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Шрифты
FONT = pygame.font.SysFont("Arial", 18)
TEXT_FONT = pygame.font.SysFont("Arial", 24)

# ================= СОСТОЯНИЯ =================

clock = pygame.time.Clock()
running = True

drawing = False          # рисуем ли сейчас
mode = "pen"             # текущий инструмент
color = BLACK            # текущий цвет
brush_size = 5           # размер кисти

start_pos = (0, 0)       # начало фигуры
last_pos = (0, 0)        # последняя точка (для pen)

# ================= ТЕКСТ =================

text_active = False      # ввод текста активен
text_content = ""        # сам текст
text_pos = (0, 0)        # позиция текста

# ================= UNDO / REDO =================

undo_stack = []  # история действий
redo_stack = []

def save_state():
    # сохраняем текущее состояние холста
    undo_stack.append(canvas.copy())
    if len(undo_stack) > 30:
        undo_stack.pop(0)  # ограничение памяти
    redo_stack.clear()

def undo():
    # отмена действия
    if undo_stack:
        redo_stack.append(canvas.copy())
        last = undo_stack.pop()
        canvas.blit(last, (0, 0))

def redo():
    # возврат действия
    if redo_stack:
        undo_stack.append(canvas.copy())
        last = redo_stack.pop()
        canvas.blit(last, (0, 0))

# ================= ИНСТРУМЕНТЫ =================

def flood_fill(surface, x, y, new_color):
    # заливка области (как ведро)
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return

    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()

        # проверка границ
        if 0 <= cx < WIDTH and 0 <= cy < HEIGHT:
            if surface.get_at((cx, cy)) == target_color:
                surface.set_at((cx, cy), new_color)

                # добавляем соседние пиксели
                stack.extend([
                    (cx+1, cy), (cx-1, cy),
                    (cx, cy+1), (cx, cy-1)
                ])

def draw_shape(surface, mode, color, start, end, size):
    # рисование фигур
    if mode == "line":
        pygame.draw.line(surface, color, start, end, size)

    elif mode == "rect":
        x = min(start[0], end[0])
        y = min(start[1], end[1])
        w = abs(start[0] - end[0])
        h = abs(start[1] - end[1])
        pygame.draw.rect(surface, color, (x, y, w, h), size)

    elif mode == "circle":
        r = int(math.hypot(end[0]-start[0], end[1]-start[1]))
        pygame.draw.circle(surface, color, start, r, size)

    elif mode == "square":
        side = min(abs(end[0]-start[0]), abs(end[1]-start[1]))
        x = start[0] if end[0] > start[0] else start[0] - side
        y = start[1] if end[1] > start[1] else start[1] - side
        pygame.draw.rect(surface, color, (x, y, side, side), size)

    elif mode == "right_tri":
        pygame.draw.polygon(surface, color,
            [start, (start[0], end[1]), end], size)

    elif mode == "rhombus":
        mx = (start[0]+end[0]) // 2
        my = (start[1]+end[1]) // 2
        pts = [(mx, start[1]), (end[0], my),
               (mx, end[1]), (start[0], my)]
        pygame.draw.polygon(surface, color, pts, size)

# ================= ПАНЕЛЬ =================

colors_palette = [
    (0,0,0), (255,0,0), (0,255,0), (0,0,255),
    (255,255,0), (255,165,0), (128,0,128), (255,255,255)
]

color_rects = []

# создаём кнопки цветов
for i, c in enumerate(colors_palette):
    color_rects.append(
        (c, pygame.Rect(10 + i*35, HEIGHT + 75, 30, 30))
    )

def draw_ui():
    # фон панели
    pygame.draw.rect(screen, GRAY, (0, HEIGHT, WIDTH, toolbar_height))

    # инфо о режиме
    msg = f"Mode: {mode.upper()} | Size: {brush_size} | Color: {color}"
    screen.blit(FONT.render(msg, True, BLACK), (10, HEIGHT + 5))

    # список инструментов
    tools_msg = "P: Pen | L: Line | R: Rect | C: Circle | S: Square | T: Tri | H: Rhombus | F: Fill | X: Text | E: Eraser"
    screen.blit(FONT.render(tools_msg, True, BLACK), (10, HEIGHT + 25))

    # доп функции
    edit_msg = "1,2,3: Size | Ctrl+Z Undo | Ctrl+Y Redo | Ctrl+S Save"
    screen.blit(FONT.render(edit_msg, True, BLACK), (10, HEIGHT + 45))

    # рисуем кнопки цветов
    for c_val, rect in color_rects:
        pygame.draw.rect(screen, c_val, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

        # выделение выбранного цвета
        if color == c_val:
            pygame.draw.rect(screen, (0,255,255), rect, 3)

# ================= ГЛАВНЫЙ ЦИКЛ =================

while running:
    screen.fill(WHITE)

    # рисуем холст
    screen.blit(canvas, (0, 0))

    # предпросмотр фигуры
    if drawing and mode not in ["pen", "eraser", "fill", "text"]:
        draw_shape(screen, mode, color, start_pos,
                   pygame.mouse.get_pos(), brush_size)

    # отображение текста при вводе
    if text_active:
        screen.blit(TEXT_FONT.render(text_content + "|", True, color), text_pos)

    draw_ui()

    # события
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # клавиатура
        if event.type == pygame.KEYDOWN:

            ctrl_pressed = pygame.key.get_mods() & pygame.KMOD_CTRL

            # ввод текста
            if text_active:
                if event.key == pygame.K_RETURN:
                    canvas.blit(TEXT_FONT.render(text_content, True, color), text_pos)
                    text_active = False
                elif event.key == pygame.K_ESCAPE:
                    text_active = False
                elif event.key == pygame.K_BACKSPACE:
                    text_content = text_content[:-1]
                else:
                    text_content += event.unicode

            else:
                # CTRL команды
                if ctrl_pressed:
                    if event.key == pygame.K_s:
                        fname = f"paint_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                        pygame.image.save(canvas, fname)

                    elif event.key == pygame.K_z:
                        undo()

                    elif event.key == pygame.K_y:
                        redo()

                # обычные клавиши (инструменты)
                else:
                    if event.key == pygame.K_p: mode = "pen"
                    elif event.key == pygame.K_l: mode = "line"
                    elif event.key == pygame.K_r: mode = "rect"
                    elif event.key == pygame.K_c: mode = "circle"
                    elif event.key == pygame.K_s: mode = "square"
                    elif event.key == pygame.K_t: mode = "right_tri"
                    elif event.key == pygame.K_h: mode = "rhombus"
                    elif event.key == pygame.K_f: mode = "fill"
                    elif event.key == pygame.K_x: mode = "text"
                    elif event.key == pygame.K_e: mode = "eraser"

                    elif event.key == pygame.K_1: brush_size = 2
                    elif event.key == pygame.K_2: brush_size = 5
                    elif event.key == pygame.K_3: brush_size = 10

        # мышь нажата
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.pos[1] < HEIGHT:
                save_state()

                if mode == "fill":
                    flood_fill(canvas, event.pos[0], event.pos[1], color)

                elif mode == "text":
                    text_active = True
                    text_pos = event.pos
                    text_content = ""

                else:
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos

            else:
                # выбор цвета
                for c_val, rect in color_rects:
                    if rect.collidepoint(event.pos):
                        color = c_val

        # мышь отпущена
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                if mode not in ["pen", "eraser"]:
                    draw_shape(canvas, mode, color, start_pos, event.pos, brush_size)
                drawing = False

        # движение мыши
        if event.type == pygame.MOUSEMOTION and drawing:

            if mode == "pen":
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

            elif mode == "eraser":
                pygame.draw.circle(canvas, WHITE, event.pos, brush_size * 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()