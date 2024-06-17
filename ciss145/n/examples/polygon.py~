import pygame, sys, random
pygame.init()
random.seed()

WIDTH, HEIGHT = 640, 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

WHITE = (255, 255, 255)

def move(d, v, m):
    d = d + v
    if d > m:
        d = m
        v = -v
    elif d < 0:
        d = 0
        v = -v
    return d, v

BLACK = (0,0,0)


while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()

    surface.fill(BLACK)
    points = []
    for x in range(10, 600, 10):
        points += [[x,100 + random.randrange(0, 20)]]
    for x in range(600, 10, -10):
        points += [[x,300 + random.randrange(0, 20)]]
    
    pygame.draw.polygon(surface, WHITE, points)
    pygame.display.flip()
    
    pygame.time.delay(1000)
