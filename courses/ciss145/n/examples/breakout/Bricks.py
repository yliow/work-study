"""
bricks.py
"""

import pygame
pygame.init()

from CONSTANTS import *

# Colors of bricks
COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, VIOLET]

# Points for each brick color
points = {}
i = 10
for color in COLORS[::-1]:
    print "color:", color, tuple(color)
    points[tuple(color)] = i
    i = i + 10
    
# Bricks
# These are BRICK_WIDTH x BRICK_HEIGHT where the dimensions should
# divide the surface's width and height
BRICK_WIDTH = 20                    
BRICK_HEIGHT = 10
MAXROW = len(COLORS) - 1            # max row number (starting with 0)
MAXCOL = WIDTH / BRICK_WIDTH - 1    # max column number (starting with 0)

boundary = pygame.Rect(0, TOP_SPACE*2, WIDTH, len(COLORS)*BRICK_HEIGHT) # WATCHOUT! 640 hardcoded
    
def get():
    brickss = []
    brick_dicts = []
    for i in [0,1]:
        bricks = []
        brick_dict = {}
        y = TOP_SPACE * 2 # *2 for empty space so that ball can bounce on top area
        for c in range(len(COLORS)):
            x = 0
            color = COLORS[c]
            for i in range(WIDTH / BRICK_WIDTH):
                brick = {}
                brick['rect'] = pygame.Rect(x, y, BRICK_WIDTH-1, BRICK_HEIGHT-1)
                brick['color'] = color
                brick['points'] = points[tuple(color)]
                brick['alive'] = True
                bricks.append(brick)
                x = x + BRICK_WIDTH
                brick_dict[(c,i)] = brick
            y = y + BRICK_HEIGHT
        brickss.append(bricks)
        brick_dicts.append(brick_dict)
    return brickss, brick_dicts

def reset(brickss):
    for bricks in brickss:
        for brick in bricks:
            brick['alive'] = True
    return brickss
            
def draw(surface, bricks):
    for brick in bricks:
        if brick['alive']:
            draw_brick(surface, brick)

def draw_brick(surface, brick):
    pygame.draw.rect(surface, brick['color'], brick['rect'])
    pygame.draw.rect(surface, WHITE, brick['rect'], 1)

def clear_brick(surface, brick):
    pygame.draw.rect(surface, BLACK, brick['rect'])

def collides_bricks(bricks, rect):
    return rect.colliderect(boundary)

def get_colliding_bricks(brick_dict, rect):
    """
    Returns a list of bricks that collides with rect
    """
    mincol = rect.x / BRICK_WIDTH - 1
    if mincol < 0: mincol = 0
    maxcol = (rect.x + rect.width) / BRICK_WIDTH + 1
    if maxcol > MAXCOL: maxcol = MAXCOL
    minrow = (rect.y - 2 * TOP_SPACE) / BRICK_HEIGHT - 1
    if minrow < 0: minrow = 0
    maxrow = (rect.y + rect.height - 2 * TOP_SPACE) / BRICK_HEIGHT + 1
    if maxrow > MAXROW: maxrow = MAXROW
    bricks = []
    for r in range(minrow, maxrow+1):
        for c in range(mincol, maxcol+1):
            bricks.append(brick_dict[(r,c)])
    return bricks

def none_alive(bricks):
    for brick in bricks:
        if brick['alive']:
            return False
    return True
