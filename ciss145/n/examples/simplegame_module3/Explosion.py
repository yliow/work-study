# file: Explosion.py

import pygame
pygame.init()

from CONSTANTS import *

# Explosion sound
def get_explosion():
    explosion = {}
    explosion["sound"] = pygame.mixer.Sound("gexplode.wav")
    explosion["played"] = False
    return explosion
