import math
from active import Active
from physical import Physical

class Animal(Active, Physical):

    is_swimming = True
    speed_x = 0
    speed_y = 0
    angle = 0
    total_speed = 2

    def __init__(self, x, y, r):
        Physical.__init__(self, x, y, r)
        return

    def move(self, x, y):
        Physical.move(self, x, y)
        return

    def rotate(self):
        # self.speed_x = self.total_speed*math.sin(self.angle)
        # self.speed_y = self.total_speed*math.cos(self.angle)
        # self.angle += 0.1
        return
