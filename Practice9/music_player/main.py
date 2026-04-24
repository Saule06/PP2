import pygame
import os
import random

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

music_dir = "musics"

music_files = [
    f for f in os.listdir(music_dir)
    if f.endswith(".mp3")
]

background_files = [
    "images/bg2.jpg",
    "images/bg1.jpg",
    "images/bg3.jpg"
]

current = 0
playing = False
paused = False

background = None
lyrics = []


# ================= MUSIC =================

def load_music():
    path = os.path.join(
        music_dir,
        music_files[current]
    )
    pygame.mixer.music.load(path)


def load_background():
    global background

    background = pygame.image.load(
        background_files[current]
    )

    background = pygame.transform.scale(
        background,
        (900, 600)
    )


def load_lyrics():

    global lyrics

    lyrics = []

    

    if not music_files:
        return

    song_name = music_files[current]

    lyric_file = song_name.replace(".mp3", ".lrc")

    path = os.path.join(music_dir, lyric_file)

    if not os.path.exists(path):
        print("Lyrics file not found:", path)
        return

    with open(path, "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith("[") and "]" in line:

                time_part = line[1:6]
                text = line.split("]")[1]

                minutes = int(time_part[:2])
                seconds = int(time_part[3:5])

                total_seconds = minutes * 60 + seconds

                lyrics.append(
                    (total_seconds, text)
                )


def play():
    global playing, paused

    if not pygame.mixer.music.get_busy():
        load_music()

    pygame.mixer.music.play()

    playing = True
    paused = False


def stop():
    global playing, paused

    pygame.mixer.music.stop()

    playing = False
    paused = False


def next_song():
    global current

    current = (
        current + 1
    ) % len(music_files)

    load_music()
    load_background()
    load_lyrics()

    play()


def prev_song():
    global current

    current = (
        current - 1
    ) % len(music_files)

    load_music()
    load_background()
    load_lyrics()

    play()


# ================= VISUALIZER =================

def draw_visualizer():

    if playing and not paused:

        num_bars = 25
        bar_width = 3
        spacing = 5

        total_width = num_bars * (bar_width + spacing)
        start_x = (900 - total_width) // 8

        center_y = 510

        for i in range(num_bars):

            height = random.randint(20, 80)

            x = start_x + i * (bar_width + spacing)

            color = (
                min(255, 150 + i * 2),
                50,
                max(0, 200 - i * 3)
            )

            pygame.draw.rect(
                screen,
                color,
                (
                    x,
                    center_y - height // 2,
                    bar_width,
                    height
                )
            )


# ================= LYRICS DISPLAY =================

def draw_lyrics():

    if not playing:
        return

    current_time = pygame.mixer.music.get_pos() / 1000

    current_line = ""
    next_line = ""

    for i in range(len(lyrics)):

        time, text = lyrics[i]

        if i == len(lyrics) - 1:

            if current_time >= time:
                current_line = text

        else:

            next_time = lyrics[i + 1][0]

            if time <= current_time < next_time:

                current_line = text
                next_line = lyrics[i + 1][1]

    # текущая строка (подсветка)
    if current_line:

        current_surface = font.render(
            current_line,
            True,
            (255, 255, 0)
        )

        rect = current_surface.get_rect(
            center=(450, 470)
        )

        screen.blit(
            current_surface,
            rect
        )

    # следующая строка
    if next_line:

        next_surface = font.render(
            next_line,
            True,
            (200, 200, 200)
        )

        rect2 = next_surface.get_rect(
            center=(450, 500)
        )

        screen.blit(
            next_surface,
            rect2
        )


# ================= INITIAL LOAD =================

if music_files:

    load_music()
    load_background()
    load_lyrics()


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:

                if not playing:
                    play()

                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False

            elif event.key == pygame.K_s:
                stop()

            elif event.key == pygame.K_n:
                next_song()

            elif event.key == pygame.K_b:
                prev_song()

            elif event.key == pygame.K_SPACE:

                if playing and not paused:

                    pygame.mixer.music.pause()
                    paused = True

                elif playing and paused:

                    pygame.mixer.music.unpause()
                    paused = False

            elif event.key == pygame.K_q:
                running = False

    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill((255, 255, 255))

    title = font.render(
        "Playlist Is",
        True,
        (0, 0, 0)
    )

    screen.blit(title, (220, 20))

    controls = font.render(
        "P-Play  S-Stop  N-Next  B-Back  SPACE-Pause",
        True,
        (10, 10, 10)
    )

    screen.blit(controls, (40, 60))

    draw_visualizer()

    draw_lyrics()

    pygame.display.flip()

    clock.tick(12)

pygame.quit()