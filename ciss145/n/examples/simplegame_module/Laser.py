import pygame
pygame.init()

from CONSTANTS import *

# Ship's laser
def get_laser():
    laser = {}
    laser["rect"] = pygame.Rect(0, 0, 4, 8)
    laser["speed"] = [0, 0]
    laser["alive"] = False
    laser["sound"] = pygame.mixer.Sound("laser.wav")
    return laser
