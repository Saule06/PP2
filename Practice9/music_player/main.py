import pygame
from player import MusicPlayer


def main():
    pygame.init()
    pygame.mixer.init()

    WIDTH = 800
    HEIGHT = 400

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")

    player = MusicPlayer(screen, WIDTH, HEIGHT)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play_music()
                elif event.key == pygame.K_s:
                    player.stop_music()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.previous_track()
                elif event.key == pygame.K_q:
                    running = False

        player.draw()
        pygame.display.flip()
        clock.tick(30)

    pygame.mixer.music.stop()
    pygame.quit()


if __name__ == "__main__":
    main()