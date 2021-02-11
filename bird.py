import pygame


class Bird:
    def __init__(self, id, height):
       self.id = id 
       self.size = height*0.03
       self.x = 100
       self.y = 100
       self.color = (255,255,255)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
