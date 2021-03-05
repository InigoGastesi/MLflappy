import pygame
import math
from nn import Net
import torch
import numpy as np

class Bird:
    def __init__(self, means=np.array([0,0,0,0], ndmin=2), sd=np.array([1.0,1.0,1.0,1.0], ndmin=2)):
       self.id = id 
       self.size = 15
       self.x = 100
       self.y = 100
       self.color = (255,255,255)
       self.speed = -0.5
       self.points = 0.0 
       self.hit = False
       self.net = Net()
       self.setWeights(means, sd)
       

    def draw(self, screen):
        if(self.y <= 0):
            self.y = 0
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    
    def move(self, rectY, rectX):
        if(not self.hit):
            self.speed = self.speed - 0.2
            self.y = self.y - self.speed
            self.points = self.points + 0.1
        input = torch.tensor([self.y/500,self.speed/10.6, rectY/500, rectX/700])
        output = self.net.fordward(input)
        x = round(output.item())
        if(x==0):
            self.up()
        

    
    def up(self):
        self.speed = 5.0
    
    def getWeights(self):
        return self.net.getWeights().tolist()

    def setWeights(self, means, sd):
        self.net.setWeights(means, sd)
   
