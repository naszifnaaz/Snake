#Classic Snake game using python and pygame

import pygame
import math
import random
from tkinter import messagebox

#Game Values
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

WIDTH = 500
HEIGHT = 500

COLS = 25
ROWS = 20

#Cube Class
class cube():
    rows = 0
    width = 0

    def __init__(self, start, dirnx = 1, dirny = 0, color = RED):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
    
    def draw(self, surface, eyes = False):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))

        #Drawing eyes
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, BLACK, circleMiddle, radius)
            pygame.draw.circle(surface, BLACK, circleMiddle2, radius)

#Snake class
class snake(object):

    body = []
    turns = []

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i,c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0]. turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                c.move(c,dirnx,c.dirny)


    def reset(self, pos):
        pass
    
    def add_cube(self):
        pass
    
    def draw(self, surface):
        for i,c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

def draw_grid(width, rows, surface):
    gap = width // rows
    
    x = 0
    y = 0
    for line in range(rows):
        x = x + gap
        y = y + gap

        pygame.draw.line(surface, BLACK, (x, 0), (x, width))
        pygame.draw.line(surface, BLACK, (0, y), (width, y))


def redraw_window():
    global win
    win.fill(WHITE)
    draw_grid(WIDTH, ROWS, surface)
    s.draw(win)
    snak.draw(win)
    pygame.display.update()

def snack(rows, items):
    positions = item.body
    while True:
        x = random.randrange(1,rows-1)
        y = random.randrange(1,rows-1)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
               continue
        else:
               break
    retur (x, y)
    

def main():
    global s, snack, win
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    FPS = 10
    s = snake(RED, (10,10))
    run = True
    
    while(run):
        pygame.time.delay(50)
        clock.tick(FPS)
        s.nove()
        redraw_window(win)

    pass

main()