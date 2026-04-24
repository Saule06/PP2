import pygame
import random 
from color_palette import *

pygame.init()

WIDTH=800
HEIGHT=800
screen=pygame.display.set_mode((WIDTH, HEIGHT))

CELL=20

def draw_grid():
    for i in range(HEIGHT//CELL):
        for j in range(WIDTH//CELL):
            pygame.draw.rect(screen, colorGRAY,
                        (i*CELL, j*CELL, CELL,CELL),1)
            


def draw_grid_chess():
    colors=[colorWHITE, colorGRAY]
    for i in range(HEIGHT//CELL):
        for j in range(WIDTH//CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body=[Point(10,11), Point(10,12), Point(10,13)]
        self.dx=1
        self.dy=0
    def move(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy