import pygame
from tail import Tail
from displayable import Displayable
from active import Active
from physical import Physical

class Fish(Displayable, Active, Physical):

    tail = Tail()
    is_swimming = True
    speed_x = 2
    speed_y = 2
    __sin = 0.0 # direction of swimming

    def __init__(self, x, y, r):
        super(Physical, self).__init__()
        print("Tworze rybke z parametrami:")
        print(self.get_x())
        print(self.get_y())
        tail = Tail(self)
        is_swimming = True
        return

    def display(self, output):
        self.tail.display(output)
        return

    def swim(self):
        self.move(self.speed_x, self.speed_y)
        self.tail.activity()
        return

    def activity(self):
        if self.is_swimming:
            self.swim()

        return
