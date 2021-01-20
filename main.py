import pygame
import src.functions as func

# Constants
SCREEN_SIZE = (800,600)

screen = pygame.display.set_mode(SCREEN_SIZE)

# Variable


# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            func.Quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                func.Quit() 
