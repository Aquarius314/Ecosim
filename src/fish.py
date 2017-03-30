import pygame
from tail import Tail
from displayable import Displayable
from active import Active
from physical import Physical

class Fish(Displayable, Active, Physical):

    is_swimming = True
    speed_x = -2
    speed_y = 0
    __sin = 0.0 # direction of swimming

    def __init__(self, x, y, r):
        Physical.__init__(self, x, y, r)
        print("Tworze rybke z parametrami:")
        print(self.get_x())
        print(self.get_y())
        self.tail = Tail(self)
        is_swimming = True
        return

    def display(self, output):
        self.tail.display(output)
        return

    def swim(self):
        self.move(self.speed_x, self.speed_y)
        print("Rybka: x=%d, y=%d" % (self.get_x(), self.get_y()))
        self.tail.activity()
        print("Ogon: x=%d, y=%d" % (self.tail.get_x(), self.tail.get_y()))
        return

    def move(self, x, y):
        Physical.move(self, x, y)
        self.tail.move(x, y)
        return

    def activity(self):
        if self.is_swimming:
            self.swim()
        return
