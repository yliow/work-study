import sys, pygame
pygame.init()

from CONSTANTS import *

def get():
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Breakout!')
    icon = pygame.image.load("w.bmp")
    pygame.display.set_icon(icon)
    return surface

def toggle(surface, surface_type):
    """
    Function used to toggle between non-full and full screen modes.
    """
    if surface_type == 0:
        surface_type = 1
        surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    else:
        surface_type = 0
        surface = pygame.display.set_mode((WIDTH, HEIGHT))
    return surface, surface_type

