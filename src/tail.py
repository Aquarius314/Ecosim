import pygame
from displayable import Displayable
from circle import Circle
from active import Active

class Tail(Displayable, Active):

    circles = []
    circles.append(Circle((200,0,0), (100,100), 10))
    circles.append(Circle((200,0,0), (118,100), 8))
    circles.append(Circle((200,0,0), (132,100), 6))
    circles.append(Circle((200,0,0), (142,100), 4))

    def wave(self):
        pass

    def activity(self):
        self.wave()
        print("Tail activity")

    def display(self, output):
        for circle in self.circles:
            circle.display(output)

# functionality: displaying waving tail animation using sine function
