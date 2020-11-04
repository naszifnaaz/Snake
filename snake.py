#Classic Snake game using python and pygame

import pygame
import math
import random
from tkinter import messagebox

#Game Values
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

#Cube Class
class cube(object):
    rows = 0
    width = 0

    def __init__(self, start, dirnx = 1, dirny = 0, color = RED):
        pass
    
    def move(self, dirnx, dirny):
        pass
    
    def draw(Self, surface, eyes = False):
        pass


#Snake class
class snake(object):

    def __init__(self, color, pos):
        pass
    
    def move(self):
        pass

    def reset(self, pos):
        pass
    
    def add_cube(self):
        pass
    
    def draw(self, surface):
        pass

def draw_grid(width, rows, surface):
    gap = width // rows
    
    x = 0
    y = 0
    for line in range(rows):
        x = x + gap
        y = y + gap

        pygame.draw.line(surface, WHITE, (x, 0), (x, width))
        pygame.draw.line(surface, WHITE, (0, y), (width, y))

    pass

def redraw_window(surface):
    global rows, width
    surface.fill(BLACK)
    draw_grid(width, rows, surface)
    pygame.display.update()
    pass

def snack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    FPS = 10
    s = snake(RED, (10,10))
    run = True
    

    while(run):
        pygame.time.delay(50)
        clock.tick(FPS)
        redraw_window(win)

    pass

main()