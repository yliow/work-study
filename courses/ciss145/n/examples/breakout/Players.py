import sys, pygame, random
pygame.init()
pygame.font.init()

# My files
from CONSTANTS import *

font = pygame.font.Font(None, 24)
def draw_scores(surface, player):
    surface.blit(player['image'], player['rect'])
    scoreimage = font.render(str(player['score']), 0, WHITE)
    scorerect = player['rect'].move(0,24)
    surface.fill(BLACK, scorerect)
    surface.blit(scoreimage, scorerect)


key_action = {
    pygame.K_LEFT: LEFT,
    pygame.K_RIGHT: RIGHT,
    pygame.K_TAB: TOGGLE,
    pygame.K_ESCAPE: QUIT,
    pygame.K_1: START_ONE_PLAYER,
    pygame.K_2: START_TWO_PLAYER,
    pygame.K_UP: SPEEDUP,
    pygame.K_DOWN: SLOWDOWN,
    pygame.K_p: PAUSE,
    }

def get_action():
    """Return an action code based on keypressed"""
    action = None
    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_LEFT]:
        action = LEFT
    elif keypressed[pygame.K_RIGHT]:
        action = RIGHT
    elif keypressed[pygame.K_TAB]:
        action = TOGGLE
    elif keypressed[pygame.K_ESCAPE]:
        sys.exit()
    elif keypressed[pygame.K_p]:
        action = PAUSE
    elif keypressed[pygame.K_UP]:
        action = SPEEDUP
    elif keypressed[pygame.K_DOWN]:
        action = SLOWDOWN
    elif keypressed[pygame.K_1]:
        action = START_ONE_PLAYER
    elif keypressed[pygame.K_2]:
        action = START_TWO_PLAYER
    return action

def get():
    player1 = {}
    player1['image'] = font.render("Player 1", 0, WHITE)
    player1['rect'] = player1['image'].get_rect()
    player1['score'] = 0

    player2 = {}
    player2['image'] = font.render("Player 2", 0, WHITE)
    player2['rect'] = player2['image'].get_rect()
    player2['rect'] = player2['rect'].move([WIDTH - player2['rect'].right + player2['rect'].left, 0])
    player2['score'] = 0

    players = [player1, player2]
    return players

def reset(players):
    players[0]['score'] = 0
    players[1]['score'] = 0
    return players
