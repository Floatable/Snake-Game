import pygame
from pygame import *
pygame.init()
screen = pygame.display.set_mode((560, 240))
clock = pygame.time.Clock()
pygame.display.set_caption("Get to the red square!")

class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

walls = []  # List to hold the walls

# Holds the level layout in a list of strings.
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W    W                            W",
    "W    W      WWWWWW                W",
    "W   WWWW       W                  W",
    "W   W        WWWW       wwwwww    W",
    "W WWW  WWWW                       W",
    "W   W     W W                     W",
    "WE  W     W   WWWWW               W",
    "W   WWW WWW   W W W               W",
    "W     W   W   W W WWWWW           W",
    "WWW   W   WWWWW W     W           W",
    "W W      WW           WWWWWWWWW   W",
    "W W   WWWW   WWW                  W",
    "W     W        W                  W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0