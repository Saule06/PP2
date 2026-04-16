import pygame
import os


class MusicPlayer:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.bg_color = (30, 30, 30)
        self.text_color = (255, 255, 255)
        self.highlight_color = (0, 200, 255)

        self.font = pygame.font.SysFont("Arial", 28, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 22)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.music_folder = os.path.join(base_dir, "music", "sample_tracks")

        self.tracks = self.load_tracks()
        self.current_track_index = 0
        self.is_playing = False
        self.error_message = ""

    def load_tracks(self):
        tracks = []

        print("Current working directory:", os.getcwd())
        print("Music folder path:", self.music_folder)
        print("Exists:", os.path.exists(self.music_folder))
        print("Is directory:", os.path.isdir(self.music_folder))

        if not os.path.exists(self.music_folder):
            print("Folder not found:", self.music_folder)
            return tracks

        if not os.path.isdir(self.music_folder):
            print("This is not a folder:", self.music_folder)
            return tracks

        for file in os.listdir(self.music_folder):
            if file.endswith(".mp3") or file.endswith(".wav"):
                full_path = os.path.join(self.music_folder, file)
                tracks.append(full_path)

        tracks.sort()
        print("Loaded tracks:", tracks)
        return tracks

    def play_music(self):
        if not self.tracks:
            self.error_message = "No tracks found"
            return

        try:
            pygame.mixer.music.load(self.tracks[self.current_track_index])
            pygame.mixer.music.play()
            self.is_playing = True
            self.error_message = ""
        except Exception as e:
            self.is_playing = False
            self.error_message = f"Cannot play file: {os.path.basename(self.tracks[self.current_track_index])}"
            print("Play error:", e)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if self.tracks:
            self.current_track_index = (self.current_track_index + 1) % len(self.tracks)
            self.play_music()

    def previous_track(self):
        if self.tracks:
            self.current_track_index = (self.current_track_index - 1) % len(self.tracks)
            self.play_music()

    def get_current_track_name(self):
        if not self.tracks:
            return "No tracks found"
        return os.path.basename(self.tracks[self.current_track_index])

    def get_track_position(self):
        position_ms = pygame.mixer.music.get_pos()
        if position_ms < 0:
            return 0
        return position_ms // 1000

    def draw(self):
        self.screen.fill(self.bg_color)

        title = self.font.render("Music Player", True, self.highlight_color)
        self.screen.blit(title, (30, 20))

        controls = self.small_font.render(
            "P - Play | S - Stop | N - Next | B - Back | Q - Quit",
            True,
            self.text_color
        )
        self.screen.blit(controls, (30, 80))

        current_track = self.small_font.render(
            f"Current Track: {self.get_current_track_name()}",
            True,
            self.text_color
        )
        self.screen.blit(current_track, (30, 140))

        status = "Playing" if self.is_playing else "Stopped"
        status_text = self.small_font.render(
            f"Status: {status}",
            True,
            self.text_color
        )
        self.screen.blit(status_text, (30, 180))

        position = self.get_track_position()
        position_text = self.small_font.render(
            f"Position: {position} sec",
            True,
            self.text_color
        )
        self.screen.blit(position_text, (30, 220))

        if self.error_message:
            error_text = self.small_font.render(
                self.error_message,
                True,
                (255, 80, 80)
            )
            self.screen.blit(error_text, (30, 320))

        pygame.draw.rect(self.screen, (100, 100, 100), (30, 280, 500, 20))
        pygame.draw.rect(
            self.screen,
            self.highlight_color,
            (30, 280, min(position * 10, 500), 20)
        )

        playlist_title = self.small_font.render("Playlist:", True, self.text_color)
        self.screen.blit(playlist_title, (580, 80))

        for i, track in enumerate(self.tracks):
            name = os.path.basename(track)
            color = self.highlight_color if i == self.current_track_index else self.text_color
            track_text = self.small_font.render(name, True, color)
            self.screen.blit(track_text, (580, 120 + i * 30))