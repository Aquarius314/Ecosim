import pygame
from tail import Tail
import world
import window

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((world.screen_width, world.screen_height))

running = True
counter = 0
window = window.Window()

def display_screen():
    pygame.display.update()
    clock.tick(60)
    screen.fill((0, 0, 255))    # BACKGROUND
    window.display(screen)
    return

    ## MAIN LOOP

while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # autoclose
    #if counter > 300:
    #    running = False # close window after some ticks

    # actions and calculations
    window.world.calculate()

    counter += 1
    display_screen()


pygame.quit()
