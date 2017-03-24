import pygame
from tail import Tail
from displayable import Displayable
from active import Active

class Fish(Displayable, Active):

    tail = Tail()

    def display(self, output):
        self.tail.display(output)
        return

    def activity(self):
        self.tail.activity()
        return
