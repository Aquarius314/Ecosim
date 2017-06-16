import math
import pygame
import random

from tail import Tail
from animal import Animal
# from active import Active
# from physical import Physical

class Fish(Animal):

    __sin = 0.0 # direction of swimmin
    sight_range = 80
    color = (200,0,0)
    energy = 300

    def __init__(self, x, y, r):
        Animal.__init__(self, x, y, r)
        is_swimming = True
        self.tail = Tail(self)
        self.destination_x = x
        self.destination_y = y
        return

    def display(self, output):
        drawX = int(self.get_x())
        drawY = int(self.get_y())
        pygame.draw.circle(output, (255,0,0), (drawX, drawY), self.sight_range, 2)
        pygame.draw.circle(output, self.color, (drawX, drawY), 10)
        # self.tail.display(output)
        return

    def set_parent(self, parent):
        self.parent_world = parent

    def swim(self):
        Animal.rotate(self)
        self.move(self.speed_x, self.speed_y)
        # self.tail.activity()
        return

    def floating(self):
        # self.speed_x = random.randint(-1,1)
        # self.speed_y = random.randint(-1,1)
        # self.move(self.speed_x, self.speed_y)
        return

    def move(self, x, y):
        Animal.move(self, x, y)
        self.tail.move(x, y)
        return

    def eat_food(self, food):
        self.energy += 100
        return

    def search_food(self):
        min_dist = self.sight_range # to make sure distance will be smaller
        food_found = False
        # self.is_swimming = True
        fx = 0
        fy = 0
        for f in self.parent_world.food:
            distance = math.sqrt((f.get_x()-self.get_x())**2 + (f.get_y()-self.get_y())**2)
            if distance < min_dist:
                # food in sight range and closer than previous food
                min_dist = distance
                food_found = True
                fx = f.get_x()
                fy = f.get_y()
                if distance < 3:
                    self.eat_food(f)
                    self.parent_world.food.remove(f)
        if food_found:
            # self.is_swimming = False
            self.destination_x = fx
            self.destination_y = fy
        return

    def go_to_destination(self):
        x = self.destination_x
        y = self.destination_y
        self.speed_x = 0
        self.speed_y = 0
        if x > self.get_x():
            self.speed_x = 1
        if x < self.get_x():
            self.speed_x = -1
        if y > self.get_y():
            self.speed_y = 1
        if y < self.get_y():
            self.speed_y = -1
        return

    def reproduce(self):
        return

    def activity(self):
        if self.is_swimming:
            self.swim()
        # else:
            # self.floating()

        self.search_food()

        self.go_to_destination()

        self.energy -= 1

        print("Energy: %d" % self.energy)

        if self.energy <= 0:
            self.parent_world.fish.remove(self)

        if self.energy >= 1000:
            self.reproduce()

        return
