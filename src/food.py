import pygame
from physical import Physical

radius = 3

class Food(Physical):

    def __init__(self, x, y):
        Physical.__init__(self, x, y, 0)
        return

    def display(self, output):
        drawX = int(self.get_x())
        drawY = int(self.get_y())
        pygame.draw.circle(output, (0,0,0), (drawX, drawY), radius)
        return
