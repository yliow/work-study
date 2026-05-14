import pygame, random
pygame.init()
random.seed()

from CONSTANTS import *
from util import *

# Create alien
def get_alien():
    alien = {}
    alien["image"] = pygame.image.load("GalaxianAquaAlien.gif")
    alien["rect"] = alien["image"].get_rect()
    alien["rect"] = alien["rect"].move([0, SCORE_HEIGHT])
    alien["speed"] = [1, 0]
    return alien

ALIEN_Y_INCREMENT = 10

def move_alien(alien):
    alien["rect"].x, alien["speed"][0] = move(alien["rect"].x,
                                      alien["speed"][0], WIDTH - alien["rect"].w)
    if random.randrange(100) == 0:
        alien["rect"].y = alien["rect"].y + ALIEN_Y_INCREMENT
    return alien
