import pygame
from displayable import Displayable

class Circle(Displayable):

    # Surface - main screen (output)
    color = (200, 0, 0)
    pos = (100, 100)
    radius = 10
    width = 0

    def __init__(self):
        return

    def __init__(self, color=(200,0,0), pos=(100,100), radius=10, width=0):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
        return

    def display(self, output):
        pygame.draw.circle(output, self.color, self.pos, self.radius, self.width)
        return

    def move_to(self, x, y):
        pos = (x, y)
        return

    def move(self, x, y):
        pos = pos + (x, y)
        return


# functionality: custom wrapper class for pygame.draw.circle()
