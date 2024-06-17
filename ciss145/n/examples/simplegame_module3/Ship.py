# file: Ship.py

import pygame
from CONSTANTS import *
import util

# Create flagship
def get_ship():
    ship = {}
    ship["image"] = pygame.image.load("GalaxianGalaxip.gif")
    ship["rect"] = ship["image"].get_rect()
    x = (WIDTH - ship["rect"].w) / 2
    y = HEIGHT - ship["rect"].h
    ship["rect"] = ship["rect"].move([x,y])
    ship["speed"] = [0, 0]
    return ship

def move(ship):
    ship["rect"].x, ship["speed"][0] = util.move(ship["rect"].x, ship["speed"][0], WIDTH - ship["rect"].w)
    ship["speed"] = [0, 0]
    return ship
