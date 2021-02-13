import pygame
import keyboard
import random
from bird import Bird
import time
import sys
from pygame.locals import *

def hitBox(bird):
    if(bird.y+15 >= 700):
        bird.color=(0,0,0)
    if(bird.y+15 >= rect2.y and bird.x+15 >= rect2.x and bird.x <= rect2.x+rwidht):
        bird.color=(0,0,0)
    if(bird.y-15 <= rect1.height and bird.x+15 >= rect1.x and bird.x <= rect1.x+rwidht):
        bird.color=(0,0,0)









(width, height) = (500,700)

xpos = 300
(rwidht, rheight) = (50, 250)

rect1 = pygame.Rect(xpos,0,rwidht,rheight)
rect2 = pygame.Rect(xpos,rheight+100,rwidht,700)

clock = pygame.time.Clock()

speed = 1.0
bird = Bird(1, height)

background = (0, 0, 0)
screen = pygame.display.set_mode((width,height))


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
    bird.move()
    if(keyboard.is_pressed('space')):
        bird.up()

    if(rect1.x < -rwidht):
        rect1.x = 550
        rect2.x = 550
        rect1.height = random.randrange(50,650)
        rect2.y = rect1.height+75
    hitBox(bird)
    clock.tick(60)
    pygame.display.update()



