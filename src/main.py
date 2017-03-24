import pygame
from tail import Tail
from world import World
from window import Window

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))

running = True
counter = 0
window = Window()

def display_screen():
    pygame.display.update()
    clock.tick(60)
    screen.fill((0, 0, 255))    # BACKGROUND
    window.display(screen)
    return


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if counter > 50:
        running = False # close window after some ticks

    # actions and calculations
    window.world.calculate()

    counter += 1
    print(counter)
    display_screen()


pygame.quit()
