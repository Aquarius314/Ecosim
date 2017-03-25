import pygame
import math
from displayable import Displayable
from circle import Circle
from active import Active

class Tail(Displayable, Active):

    circles = []
    circles.append(Circle((200,0,0), (200,300), 10))
    circles.append(Circle((200,0,0), (210,300), 8))
    circles.append(Circle((200,0,0), (218,300), 6))
    circles.append(Circle((200,0,0), (224,300), 6))
    circles.append(Circle((200,0,0), (230,300), 4))
    circles.append(Circle((200,0,0), (234,300), 4))
    __sin_clock = 0.0

    def wave(self):
        index = 0.0
        for circle in self.circles:
            index += 2.5
            wave_range = self.circles[0].get_radius()-circle.get_radius()
            real_y = wave_range*math.sin((index+self.__sin_clock)/3.0)
            circle.move_to(circle.get_x(), self.circles[0].get_y()+int(real_y))
            circle.move(-2, 0)


    def activity(self):
        self.__sin_clock += 1
        self.wave()
        return

    def display(self, output):
        for circle in self.circles:
            circle.display(output)

# functionality: displaying waving tail animation using sine function
