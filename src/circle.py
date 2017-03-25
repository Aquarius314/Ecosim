import pygame
from displayable import Displayable

class Circle(Displayable):

    # Surface - main screen (output)
    color = (200, 0, 0)
    pos = (100, 100)
    __radius = 10
    __width = 0

    def __init__(self):
        return

    def __init__(self, color=(200,0,0), pos=(100,100), radius=10, width=0):
        self.color = color
        self.pos = pos
        self.__radius = radius
        self.__width = width
        return

    def display(self, output):
        pygame.draw.circle(output, self.color, self.pos, self.__radius, self.__width)
        return

    def move_to(self, x, y):
        self.pos = (x, y)
        return

    def move(self, x, y):
        self.pos = (self.pos[0]+x, self.pos[1]+y)
        return

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def get_radius(self):
        return self.__radius


# functionality: custom wrapper class for pygame.draw.circle()
