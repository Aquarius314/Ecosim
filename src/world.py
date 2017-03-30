import pygame
from displayable import Displayable
from active import Active
from fish import Fish

class World:

    fish = Fish(200, 200, 10)

    def collect_actives(self):
        actives_list = []
        actives_list.append(self.fish)
        return actives_list

    def collect_displayables(self):
        displayables_list = []
        displayables_list.append(self.fish)
        return displayables_list

    def calculate(self):
        for active in self.collect_actives():
            active.activity()
        return

# functionality: space for all the living gamephysicals. Stores fish and predators
# this is the heart of the ecosystem
