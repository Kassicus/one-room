import pygame
from random import randint

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

class Color():
    def __init__(self):
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)

    def get_random(self) -> pygame.Color:
        c = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
        return c
    
color = Color()

events = None
delta_time = 0
framerate = 120

global_offset = pygame.math.Vector2()