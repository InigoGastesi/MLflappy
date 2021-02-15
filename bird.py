import pygame


class Bird:
    def __init__(self, id, height):
       self.id = id 
       self.size = 15
       self.x = 100
       self.y = 100
       self.color = (255,255,255)
       self.speed = -0.5
       self.points = 0.0 
       self.hit = False

    def draw(self, screen):
        if(self.y <= 0):
            self.y = 0
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    
    def move(self):
        if(not self.hit):
            self.speed = self.speed - 0.2
            self.y = self.y - self.speed
            self.points = self.points + 0.1
    
    def up(self):
        self.speed = 5.0
