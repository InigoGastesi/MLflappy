import pygame
from bird import Bird
import time
import sys
from pygame.locals import *
(width, height) = (500,700)

xpos = 300
(rwidht, rheight) = (50, 250)

rect1 = pygame.Rect(xpos,0,rwidht,rheight)
rect2 = pygame.Rect(xpos,rheight+75,rwidht,700)

clock = pygame.time.Clock()

speed = 1.0
bird = Bird(1, height)

background = (0, 0, 0)
screen = pygame.display.set_mode((width,height))
screen.fill(background)





while True:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    bird.draw(screen)
    pygame.draw.rect(screen, (255,255,255), rect1)
    pygame.draw.rect(screen, (255,255,255), rect2)
    rect1.move_ip(-speed,0)
    rect2.move_ip(-speed,0)
    clock.tick(60)
    pygame.display.update()
