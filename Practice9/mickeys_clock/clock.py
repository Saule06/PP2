import pygame
import os
import math
from datetime import datetime


class MickeyClock:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.center_x = width // 2
        self.center_y = height // 2

        self.background_color = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 100, 255)

        self.font = pygame.font.SysFont("Arial", 32, bold=True)

        self.hand_image = self.load_hand_image()

    def load_hand_image(self):
        image_path = os.path.join("images", "mickey_hand.png")
        print("Trying to load:", image_path)
        print("File exists:", os.path.exists(image_path))

        try:
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (120, 120))
            print("Image loaded successfully")
            return image
        except Exception as e:
            print("Image load error:", e)
            return None

    def get_time(self):
        now = datetime.now()
        return now.minute, now.second

    def get_angle(self, value):
        return -90 - (value * 6)

    def draw_clock_face(self):
        pygame.draw.circle(self.screen, self.black, (self.center_x, self.center_y), 200, 4)
        pygame.draw.circle(self.screen, self.black, (self.center_x, self.center_y), 8)

        for i in range(60):
            angle = math.radians(i * 6)
            x1 = self.center_x + 180 * math.cos(angle - math.pi / 2)
            y1 = self.center_y + 180 * math.sin(angle - math.pi / 2)
            x2 = self.center_x + 195 * math.cos(angle - math.pi / 2)
            y2 = self.center_y + 195 * math.sin(angle - math.pi / 2)
            pygame.draw.line(self.screen, self.black, (x1, y1), (x2, y2), 2)

    def draw_line_hand(self, angle, length, color, width=6):
        rad = math.radians(angle)
        end_x = self.center_x + length * math.cos(rad)
        end_y = self.center_y + length * math.sin(rad)
        pygame.draw.line(
            self.screen,
            color,
            (self.center_x, self.center_y),
            (end_x, end_y),
            width
        )

    def draw_image_hand(self, angle):
        rotated_image = pygame.transform.rotate(self.hand_image, -angle - 90)
        rect = rotated_image.get_rect(center=(self.center_x, self.center_y))
        self.screen.blit(rotated_image, rect)

    def draw(self):
        self.screen.fill(self.background_color)
        self.draw_clock_face()

        minutes, seconds = self.get_time()

        minute_angle = self.get_angle(minutes)
        second_angle = self.get_angle(seconds)

        if self.hand_image is not None:
            self.draw_image_hand(minute_angle)
            self.draw_image_hand(second_angle)
        else:
            # fallback if image is broken
            self.draw_line_hand(minute_angle, 120, self.blue, 8)   # minutes
            self.draw_line_hand(second_angle, 160, self.red, 4)   # seconds

        time_text = self.font.render(f"{minutes:02}:{seconds:02}", True, self.black)
        self.screen.blit(time_text, (self.width // 2 - 50, 40))

    def update(self):
        pass