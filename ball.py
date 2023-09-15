#1a Importing packages
import pygame
from pygame.locals import *
import random

#1b Creating the Ball class
class Ball():
#1c Instantiating the Ball object
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window # remember the window, so we can draw later
        
        self.image = pygame.image.load('Asset/Trump.png')
#2 Getting the rect of the image and determining its minimum and maximum width and height values.
    # A rect is made up of [x, y, width, height]
        ballRect = self.image.get_rect()
        self.width = ballRect[2]
        self.height = ballRect[3]
        
        self.max_width = windowWidth - self.width
        self.max_height = windowHeight - self.height

#3 Picking a random strating pos
        self.x = random.randrange(0, self.max_width)
        self.y = random.randrange(0, self.max_height)
        
#4 Choosing a random speed between -4 and 4, but not zero in both the x and y direction
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.x_Speed = random.choice(speedsList)
        self.y_Speed = random.choice(speedsList)
        
#5 Defining the update method
    def update(self):
        
        if self.x not in range(0, self.max_width):
            self.x_Speed *= -1
        if self.y not in range(0, self.max_height):
            self.y_Speed *= -1

            
        self.x += self.x_Speed
        self.y += self.y_Speed
        
#6 Defining the draw method
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))