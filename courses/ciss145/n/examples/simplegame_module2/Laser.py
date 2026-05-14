# file: Laser.py

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

def move_laser(laser):    
    if laser["alive"]:
        laser["rect"].y, laser["speed"][1] = move(laser["rect"].y, laser["speed"][1], HEIGHT - laser["rect"].h)
        if laser["rect"].y < SCORE_HEIGHT:
            laser["alive"] = False
