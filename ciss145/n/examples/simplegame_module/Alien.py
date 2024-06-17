import pygame
pygame.init()

from CONSTANTS import *

# Create alien
def get_alien():
    alien = {}
    alien["image"] = pygame.image.load("GalaxianAquaAlien.gif")
    alien["rect"] = alien["image"].get_rect()
    alien["rect"] = alien["rect"].move([0, SCORE_HEIGHT])
    alien["speed"] = [1, 0]
    return alien

ALIEN_Y_INCREMENT = 10
