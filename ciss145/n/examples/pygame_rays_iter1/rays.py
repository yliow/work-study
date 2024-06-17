import pygame, sys
WIDTH, HEIGHT = 640, 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

sys.stdout = file("stdout.txt", "w")
sys.stderr = file("stderr.txt", "w")

violet = pygame.Color("violet")
black = (0,0,0)

def move(d, v, m):
    d = d + v
    if d > m:
        d = m
        v = -v
    elif d < 0:
        d = 0
        v = -v
    return d, v

# End points for line 1
x, y = 50, 60
xspeed, yspeed = 2, 1
X, Y = 10, 200
Xspeed, Yspeed = 1, -2

# End points for line 2
a, b = 50, 60
aspeed, bspeed = 2, 1
A, B = 10, 200
Aspeed, Bspeed = 1, -2

FRAME_RATE = 1000.0 / 30

count = 0

while 1:

    starttime = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()

    # Move line 1
    x, xspeed = move(x, xspeed, WIDTH - 1)
    y, yspeed = move(y, yspeed, HEIGHT - 1)
    X, Xspeed = move(X, Xspeed, WIDTH - 1)
    Y, Yspeed = move(Y, Yspeed, HEIGHT - 1)

    # Move line 2 is count reaches 3
    if count >= 10:
        a, aspeed = move(a, aspeed, WIDTH - 1)
        b, bspeed = move(b, bspeed, HEIGHT - 1)
        A, Aspeed = move(A, Aspeed, WIDTH - 1)
        B, Bspeed = move(B, Bspeed, HEIGHT - 1)

    surface.fill(black)

    # Draw line 1
    pygame.draw.line(surface, violet, \
                     (x,y), (X,Y))

    # Draw line 2 if count reaches 3
    if count >= 10:
        pygame.draw.line(surface, violet, \
                         (a,b), (A,B))        
    
    pygame.display.flip()

    if count < 10:
        count = count + 1

    endtime = pygame.time.get_ticks()
    totaltime = starttime - endtime
    timeleft = int(FRAME_RATE - totaltime)
    if timeleft > 0:
        pygame.time.delay(timeleft)
