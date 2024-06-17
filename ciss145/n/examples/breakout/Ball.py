import pygame, random
pygame.init()
random.seed()

# My files
from CONSTANTS import *

WHITE = pygame.Color('white') # only used for drawing border of brick
BLACK = pygame.Color('black')

# Balls
RADIUS = 6
DIAMETER = 2 * RADIUS
VELOCITY = [2,-1]
ACCELERATION = 1

def get():
    ball = {}
    ball['rect'] = pygame.Rect(300, 300, DIAMETER, DIAMETER)
    ball['r'] = RADIUS
    ball['v'] = VELOCITY
    ball['a'] = ACCELERATION
    ball['color'] = WHITE
    return ball

from Paddle import PADDLE_HEIGHT
from CONSTANTS import HEIGHT
from CONSTANTS import WIDTH

def reset(ball):
    ball['rect'] = pygame.Rect((WIDTH - DIAMETER) / 2,
                               HEIGHT - PADDLE_HEIGHT - DIAMETER,
                               DIAMETER, DIAMETER)
    ball['v'] = [random.choice([-2,-1,1,2,3]), -2] #VELOCITY
    return ball

def draw(surface, ball):
    r = ball['r']
    x = ball['rect'].left + r
    y = ball['rect'].top + r
    pygame.draw.circle(surface, ball['color'], (x,y), r)

def move(ball):
    rect = ball['rect']
    rect = rect.move(ball['v'])
    ball['rect'] = rect
    return ball
