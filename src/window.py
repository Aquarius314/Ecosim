import pygame
from world import World
from displayable import Displayable


class Window(Displayable):

    world = World()

    def __init__(self):
        self.world = World()
        return

    def collect_displayables(self):
        displayables_list = []
        # all physicals on the screen go here
        for element in self.world.collect_displayables():
            displayables_list.append(element)

        return displayables_list


    def display(self, output):
        for disp in self.collect_displayables():
            disp.display(output)
        return


# functionality: stores window physicals (game display, user interface canvas etc)
