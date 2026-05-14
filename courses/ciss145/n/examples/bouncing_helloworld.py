import pygame, sys, random
pygame.init()
random.seed()

WIDTH, HEIGHT = 640, 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

BLACK = (0, 0, 0)

def move(d, v, m):
    d = d + v
    if d > m:
        d = m
        v = -v
    elif d < 0:
        d = 0
        v = -v
    return d, v

R = random.randrange(256)
G = random.randrange(256)
B = random.randrange(256)
Rspeed = random.randrange(1, 3)
Gspeed = random.randrange(1, 3)
Bspeed = random.randrange(1, 3)

font = pygame.font.Font(None, 100)

image = font.render("hello world", 1, BLACK)
imagerect = image.get_rect()

x = random.randrange(WIDTH - imagerect.x)
y = random.randrange(HEIGHT - imagerect.h)
xspeed = random.randrange(1, 3)
yspeed = random.randrange(1, 3)

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()

    surface.fill(BLACK)
    
    R, Rspeed = move(R, Rspeed, 255)
    G, Gspeed = move(G, Gspeed, 255)
    B, Bspeed = move(B, Bspeed, 255)
    color = (R, G, B)

    x, xspeed = move(x, xspeed, WIDTH - 1 - imagerect.w)
    y, yspeed = move(y, yspeed, HEIGHT - 1 - imagerect.h)

    surfacerect = imagerect.move([x, y])

    image = font.render("hello world", 1, color)
    surface.blit(image, surfacerect)
    
    pygame.display.flip()
    pygame.time.delay(10)
