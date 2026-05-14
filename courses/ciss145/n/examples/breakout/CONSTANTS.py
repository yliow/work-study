# CONSTANTS.py
# Contains global constants

# Screen
WIDTH = 640
HEIGHT = 480
TOP_SPACE = 50 # space for "Player" and "Score"

# Pygame colors
import pygame
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
RED = pygame.Color('red')
ORANGE = pygame.Color('orange')
YELLOW = pygame.Color('yellow')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')
PURPLE = pygame.Color('purple')
VIOLET = pygame.Color('violet')


# Game states
INIT_DEMO = 0
DEMO = 1

INIT_GAME = 2
GAMEOVER = 3
PLAY = 4
PLAYER_DIES = 5
NEXT_PLAYER = 1
NEXT_LEVEL = 2

# action
LEFT = 0
RIGHT = 1
PAUSE = 2
QUIT = 3
TOGGLE = 4
SLOWDOWN = 6
SPEEDUP = 7
START_ONE_PLAYER = 5
SLOWDOWN = 6
SPEEDUP = 7
START_TWO_PLAYER = 8

