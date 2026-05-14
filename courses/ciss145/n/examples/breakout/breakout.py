import sys, pygame, random
sys.stdout = file("stdout.txt", 'w')
sys.stderr = file("stderr.txt", 'w')

random.seed()
pygame.init()
pygame.font.init()

# My files
from CONSTANTS import *

import Surface
import Ball
import Paddle
import Bricks
import Music
import Players
from collision_detection import *

explode = pygame.mixer.Sound("sounds/gexplode.wav")
laser = pygame.mixer.Sound("sounds/laser.wav")

font = pygame.font.Font(None, 24)
bigfont = pygame.font.Font(None, 48)
playrect = pygame.Rect(0, TOP_SPACE, WIDTH, HEIGHT)

def draw_balls_left(surface, balls):
    image = font.render("Balls left: " + str(balls), 0, WHITE)
    rect = image.get_rect()
    rect = rect.move((WIDTH - rect.width) / 2, 0)
    surface.blit(image, rect)
    
def draw_gameover(surface):
    def write(s, f, y):
        image = f.render(s, 0, WHITE)
        rect = image.get_rect()
        rect = rect.move((WIDTH - rect.width) / 2, y)
        surface.blit(image, rect)

    write("Breakout!", bigfont, 200)
    write("Game Over", bigfont, 240)
    write("1 - One Player", font, 280)
    write("2 - Two Player", font, 310)
    write("Tab - Toggle full screen", font, 340)
    

def draw_getready(surface, player):
    image = bigfont.render("Get Ready Player " + str(player + 1) + "!", 0, WHITE)
    rect = image.get_rect()
    rect = rect.move((WIDTH - rect.width) / 2, 200)
    surface.blit(image, rect)

def gameloop(surface, surface_type, ball, bricks, brick_dict, player, paddle, demo, state):


    start = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Get user action from keypressed
    action = Players.get_action()
    print action, action == START_ONE_PLAYER
    
    # Check if user pause game or toggle screen
    if action == PAUSE:
        return
    elif action == TOGGLE:
        surface, surface_type = Surface.toggle(surface, surface_type)
        Players.draw_scores(surface, player)
    elif action == START_ONE_PLAYER:
        demo = False
        numplayers = 1
        state = INIT_GAME
        
    elif action == START_TWO_PLAYER:
        demo = False
        numplayers = 2
        state = INIT_GAME
        
    # Move objects
    if not demo:
        paddle = Paddle.move(paddle, action)
    else:
        """ demo case """
        paddle_mid = paddle['rect'].left + paddle['rect'].width/2
        ball_mid = ball['rect'].left + ball['rect'].width/2
        if  paddle_mid < ball_mid:
            paddle = Paddle.move(paddle, RIGHT)
        elif paddle_mid > ball_mid:
            paddle = Paddle.move(paddle, LEFT)
            
    ball = Ball.move(ball)

    # Collision detection
    collides_with = []

    # Collision with walls
    ballrect = ball['rect']
    if ballrect.left < 0:
        ball['v'][0] = -ball['v'][0]
        ballrect.left = 0
    elif ballrect.right >= WIDTH:
        ball['v'][0] = -ball['v'][0]
        ballrect.right = WIDTH

    if ballrect.top < TOP_SPACE:
        ball['v'][1] = -ball['v'][1]
        ballrect.top = TOP_SPACE
    elif ballrect.bottom >= HEIGHT:
        ball['v'][1] = -ball['v'][1]
        ballrect.bottom = HEIGHT
        state = PLAYER_DIES

    # Collision with bricks
    r = ball['r']
    ballv = ball['v']
    ballrect = ball['rect']
    ballcenter = [ballrect.x + r, ballrect.y + r]
    prev_ballcenter = [ballcenter[0] - ball['v'][0], ballcenter[1] - ball['v'][1]] 

    possible_bricks = Bricks.get_colliding_bricks(brick_dict, ballrect)
    if possible_bricks:
        
        # collision response for bricks
        collideds = get_collideds(prev_ballcenter, ballcenter, ballv, r, possible_bricks)
        if collideds:
            collideds.sort()
            min_d2, min_intersection, min_intersectionpoint, min_collided = collideds[0]
            for d2, intersection, intersectionpoint, collided in collideds:
                if d2 > min_d2: break
                if intersection == 'right':
                    ball['v'][0] = -ball['v'][0]
                    ballrect.left = collided['rect'].right + 1
                elif intersection == 'left':
                    ball['v'][0] = -ball['v'][0]
                    ballrect.right = collided['rect'].left - 1
                if intersection == 'bottom':
                    ball['v'][1] = -ball['v'][1]
                    ballrect.top = collided['rect'].bottom + 1
                elif intersection == 'top':
                    ball['v'][1] = -ball['v'][1]
                    ballrect.bottom = collided['rect'].top - 1
                elif intersection == 'corner':
                    ball['v'] = [-ball['v'][0], -ball['v'][1]]
                    ball = Ball.move(ball)
                
                collided['alive'] = False
                player['score'] = player['score'] + collided['points']
                Players.draw_scores(surface, player)
                if not demo: explode.play()

            #pygame.time.delay(200)

    elif ballrect.colliderect(paddle['rect']):
        ball['v'][1] = -ball['v'][1]
        ball['rect'].bottom = HEIGHT - Paddle.PADDLE_HEIGHT

        if not demo: laser.play()

        # add paddle velocity to ball
        paddle_v = 0
        if action == LEFT:
            paddle_v = -1
        elif action == RIGHT:
            paddle_v = 1
        ball['v'][0] += paddle_v

    surface.fill(BLACK, playrect)
    Bricks.draw(surface, bricks)
    Ball.draw(surface, ball)
    Paddle.draw(surface, paddle)
    if demo: draw_gameover(surface)
    
    pygame.display.flip()

    end = pygame.time.get_ticks()
    FR = 1000/60
    dt = end - start
    if dt > FR: pygame.time.delay(dt)

    return surface, surface_type, ball, bricks, brick_dict, player, paddle, demo, action, state

"""
two variables:
demo (boolean)
numplayers
state

                [no more bricks]
                -------------      ----
                |           |      |  |
                V           |      |  v
            init demo ---> demo game loop[demo = True]
                ^           |                                [new level]
                |           |[user starts game]             -------------  ---- 
                |           |                               |           |  |  |
                |           v                               v           |  |  v
                |       init game ---> init player ---> init game ---> game loop [demo = False] ---> exit player  ---> exit game (prompt high scorer)
                |                          ^                                                             |                          |
                |                          |                                                             |                          |
                |                          ---------------------------------------------------------------                          |
                |                                                                                                                   |
                ---------------------------------------------------------------------------------------------------------------------
               
"""
def run():
    """ initialize for welcome """
    surface_type = 0
    surface = Surface.get()

    ball = Ball.get()
    paddle = Paddle.get()
    brickss, brick_dicts = Bricks.get()
    players = Players.get()
    numplayers = 2
    player = 0
    
    demo = True
    state = INIT_DEMO
    print state
    
    while 1:

        if demo:
            if state == INIT_DEMO:
                
                Music.demo()
                ball = Ball.reset(ball)
                paddle = Paddle.reset(paddle)
                brickss = Bricks.reset(brickss)
                players = Players.reset(players)
                numplayers = 2
                player = 0
                balls_left = 2

                Players.draw_scores(surface, players[0])
                Players.draw_scores(surface, players[1])
                Bricks.draw(surface, brickss[player])
                draw_balls_left(surface, balls_left)
                state = DEMO

            elif state == DEMO:
                if Bricks.none_alive(brickss[player]):
                    state = INIT_DEMO
                else:
                    surface, surface_type, ball, brickss[player], brick_dicts[player], players[player], paddle, demo, action, state = \
                         gameloop(surface, surface_type, ball, brickss[player], brick_dicts[player], players[player], paddle, demo, state)

            else:
                print "ERROR: in demo but invalid state =", state
                sys.exit()
            
        else: # not demo mode
            
            if state == INIT_GAME:

                Music.stop()
                Music.start()
                
                players = Players.reset(players)
                brickss = Bricks.reset(brickss)
                balls_left = 2

                state = NEXT_PLAYER
                
            elif state == NEXT_PLAYER:

                paddle = Paddle.reset(paddle)
                ball = Ball.reset(ball)
                
                surface.fill(BLACK)
                Bricks.draw(surface, brickss[player])
                Ball.draw(surface, ball)
                Paddle.draw(surface, paddle)
                Players.draw_scores(surface, players[0])
                draw_balls_left(surface, balls_left)
                if numplayers == 2: Players.draw_scores(surface, players[1])

                draw_getready(surface, player)
                pygame.display.flip()

                Music.gameplay()
                time = pygame.time.get_ticks()
                while pygame.time.get_ticks()  - time < 3000: pygame.time.delay(10)
                state = PLAY

            elif state == PLAYER_DIES:
                Music.stop()
                Music.gameover()
                while pygame.time.get_ticks()  - time < 3000: pygame.time.delay(10)

                # now check if we need to load new player or end the game
                if balls_left == 0 and player == numplayers - 1:
                    state = GAMEOVER
                    pygame.time.delay(1000)
                else:
                    if player == numplayers - 1:
                        player = 0
                        balls_left -= 1
                    else:
                        player += 1
                    state = NEXT_PLAYER

            elif state == PLAY:
                surface, surface_type, ball, brickss[player], brick_dicts[player], players[player], paddle, demo, action, state = \
                 gameloop(surface, surface_type, ball, brickss[player], brick_dicts[player], players[player], paddle, demo, state)

                """ state check """
                if state != PLAY and state != PLAYER_DIES:
                    print "ERROR!!!"

            elif state == GAMEOVER:
                print "gameover"
                # maybe get high score
                demo = True
                state = INIT_DEMO
           
if __name__ == "__main__":
    run()
