import pygame
import math
from displayable import Displayable
from circle import Circle
from active import Active

class Tail(Displayable, Active):

    circles = []
    __sin_clock = 0.0

    def __init__(self, fish=None):
        if fish is not None:
            self.x = fish.get_x()
            self.y = fish.get_y()
        return

    def wave(self):
        index = 0.0
        for circle in self.circles:
            index += 2.5
            wave_range = self.circles[0].get_radius()-circle.get_radius()
            real_y = wave_range*math.sin((index+self.__sin_clock)/3.0)
            circle.move_to(circle.get_x(), self.circles[0].get_y()+int(real_y))
            circle.move(-2, 0)
        return

    def activity(self):
        self.__sin_clock += 1
        self.wave()
        return

    def display(self, output):
        for circle in self.circles:
            circle.display(output)
        return



# functionality: displaying waving tail animation using sine function
