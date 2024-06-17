import sys, pygame, random
pygame.init()
pygame.font.init()

from CONSTANTS import *

# Paddle
PADDLE_WIDTH = 50
PADDLE_HEIGHT = 10
PADDLE_COLOR = WHITE
PADDLE_SPEED = 3


def get():
    paddle = {}
    paddle['rect'] = pygame.Rect((WIDTH - PADDLE_WIDTH) / 2,
                                 HEIGHT - PADDLE_HEIGHT,
                                 PADDLE_WIDTH,
                                 PADDLE_HEIGHT)
    paddle['speed'] = PADDLE_SPEED
    paddle['color'] = WHITE
    return paddle
    
def reset(paddle):
    """Reset paddle to the middle along the width"""
    paddle['rect'] = pygame.Rect((WIDTH - PADDLE_WIDTH) / 2,
                             HEIGHT - PADDLE_HEIGHT,
                             PADDLE_WIDTH,
                             PADDLE_HEIGHT)
    return paddle
    
def draw(surface, paddle):
    pygame.draw.rect(surface, paddle['color'], paddle['rect'])

def move(paddle, action):
    LEFT = 0
    RIGHT = 1
    dt = 1
    direction = None
    if action == LEFT:
        direction = -1
    elif action == RIGHT:
        direction = 1
    if direction == None:
        return paddle
    rect = paddle['rect']
    speed = paddle['speed']
    rect = rect.move([speed * dt * direction, 0])
    if rect.left < 0:
        rect.x = 0
    elif rect.right >= WIDTH:
        rect.x = WIDTH - rect.width
    paddle['rect'] = rect
    return paddle
