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

points = []
for i in range(3):
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    xspeed = random.randrange(-1,2,2) * random.randrange(1, 3)
    yspeed = random.randrange(-1,2,2) * random.randrange(1, 3)
    points.append([(x, y), (xspeed, yspeed)])

R = random.randrange(256)
G = random.randrange(256)
B = random.randrange(256)
Rspeed = random.randrange(-1,2,2) * random.randrange(1, 3)
Gspeed = random.randrange(-1,2,2) * random.randrange(1, 3)
Bspeed = random.randrange(-1,2,2) * random.randrange(1, 3)

BLACK = (0,0,0)

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()

    for i in range(3):
        point = points[i]
        (x, y), (xspeed, yspeed) = point
        x, xspeed = move(x, xspeed, WIDTH - 1)
        y, yspeed = move(y, yspeed, HEIGHT - 1)
        points[i] = [(x, y), (xspeed, yspeed)]

    R, Rspeed = move(R, Rspeed, 255)
    G, Gspeed = move(G, Gspeed, 255)
    B, Bspeed = move(B, Bspeed, 255)
    color = (R, G, B)   
    surface.fill(BLACK)
    
    pygame.draw.polygon(surface, color, [points[0][0], points[1][0], points[2][0], points[0][0]])
    pygame.display.flip()
    pygame.time.delay(10)
