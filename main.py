import pygame
from bird import Bird

(width, height) = (1200,1000)
bird = Bird(1, height)

background = (0, 0, 0)
screen = pygame.display.set_mode((width,height))
screen.fill(background)

pygame.draw.rect(screen, (255,255,255), (250,0,200,250))
pygame.draw.rect(screen, (255,255,255), (250,0,200,250))
bird.draw(screen)

pygame.display.flip()


while True:
    pass