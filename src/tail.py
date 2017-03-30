import pygame
import math
from displayable import Displayable
from circle import Circle
from active import Active
from physical import Physical

class Tail(Displayable, Active, Physical):

    circles = []
    __sin_clock = 0.0

    def __init__(self, fish=None):
        if fish is not None:
            self.move_to(fish.get_x(), fish.get_y())
            print("Po utworzeniu wspolrzedne ogona: x=%d, y=%d" % (self.get_x(), self.get_y()))

        cir_x = self.get_x()
        cir_y = self.get_y()
        cir_r = 10
        for i in range(4):
            self.circles.append(Circle((255,0,0), (cir_x, cir_y), cir_r))
            cir_x += 15
            cir_y += 0
            cir_r -= 3


        return

    def wave(self):
        index = 0.0
        print("Ogonek: x=%d, y=%d" % (self.get_x(), self.get_y()))
        for circle in self.circles:
            index += 2.5
            wave_range = self.circles[0].get_radius()-circle.get_radius()
            real_y = wave_range*math.sin((index+self.__sin_clock)/3.0)
            circle.move_to(circle.get_x(), self.circles[0].get_y()+int(real_y))
        return

    def activity(self):
        self.__sin_clock += 1
        self.wave()
        return

    def move(self, x, y):
        Physical.move(self, x, y)
        for circle in self.circles:
            circle.move(x, y)
            print("Circle: x=%d, y=%d" % (circle.get_x(), circle.get_y()))
        return

    def display(self, output):
        for circle in self.circles:
            circle.display(output)
        return



# functionality: displaying waving tail animation using sine function
