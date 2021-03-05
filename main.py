import pygame
import keyboard
import random
from bird import Bird
import time
import sys
from pygame.locals import *
import numpy as np


def hitBox(bird):
    if(bird.y+15 >= 700):
        bird.color=(0,0,0)
        bird.hit = True
    if(bird.y+15 >= rect2.y and bird.x+15 >= rect2.x and bird.x <= rect2.x+rwidht):
        bird.color=(0,0,0)
        bird.hit = True
    if(bird.y-15 <= rect1.height and bird.x+15 >= rect1.x and bird.x <= rect1.x+rwidht):
        bird.color=(0,0,0)
        bird.hit = True


def newGen():
    weights = []
    for bird in birds:
        weights.append(bird.getWeights())    
        print(bird.getWeights()) 
    weights = np.array(weights)
    print(weights.shape)
    birds.clear()
    
    for i in range(1,100):
        birds.append(Bird(i, height))
    rect1.x = 550
    rect2.x = 550
    rect1.height = random.randrange(100,500)
    rect2.y = rect1.height+115



(width, height) = (500,700)

xpos = 500 
(rwidht, rheight) = (30, 250)

rect1 = pygame.Rect(xpos,0,rwidht,rheight)
rect2 = pygame.Rect(xpos,rheight+115,rwidht,700)

clock = pygame.time.Clock()

speed = 2.0

background = (0, 0, 0)
screen = pygame.display.set_mode((width,height))

birds = []

for i in range(1,100):
    birds.append(Bird(i, height))
    



while True:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.draw.rect(screen, (255,255,255), rect1)
    pygame.draw.rect(screen, (255,255,255), rect2)
    rect1.move_ip(-speed,0)
    rect2.move_ip(-speed,0)
    for bird in birds:
        bird.move(rect1.y, rect1.x)
        bird.draw(screen)

#    if(keyboard.is_pressed('space')):
#        bird.up()

    if(rect1.x < -rwidht):
        rect1.x = 550
        rect2.x = 550
        rect1.height = random.randrange(100,500)
        rect2.y = rect1.height+115
    
    for bird in birds:
        hitBox(bird)
        if bird.hit:
            birds.remove(bird)
        if len(birds)< 50:
            newGen()
    clock.tick(60)
    pygame.display.update()
