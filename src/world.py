import time
import random
import pygame
from displayable import Displayable
from active import Active
from fish import Fish
from food import Food

screen_width = 600
screen_height = 600

class World:

    world_time = time.time()
    fish = []
    food_time = 0
    food_per_second = 4

    food = []

    def __init__(self):
        self.world_time = time.time()
        # self.fish.set_parent(self)
        # for f in self.fish:
            # f.set_parent(self)
        # create initial fish
        for i in range(10):
            f = Fish(random.randint(0, 600), random.randint(0, 600), 10)
            f.set_parent(self)
            self.fish.append(f)
        # create initial food
        for i in range(20):
            fx = random.randint(0, screen_width)
            fy = random.randint(0, screen_height)
            self.food.append(Food(fx, fy))
        return

    def collect_actives(self):
        actives_list = list(self.fish)
        return actives_list

    def collect_displayables(self):
        displayables_list = list(self.fish)
        # TO DO: all fish
        # displayables_list.append(self.fish)

        # all food objects
        for f in self.food:
            displayables_list.append(f)

        return displayables_list

    def create_food(self):
        if time.time()*1000 - 1000/self.food_per_second > self.food_time:
            # tick
            self.food_time = time.time()*1000
            #print("Produce food\n")
            fx = random.randint(0, screen_width)
            fy = random.randint(0, screen_height)
            self.food.append(Food(fx, fy))
        return

    def calculate(self):
        for active in self.collect_actives():
            active.activity()
        self.create_food()
        return

# functionality: space for all the living gamephysicals. Stores fish and predators
# this is the heart of the ecosystem
