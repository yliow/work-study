import pygame, sys, random
pygame.init()
random.seed()

WIDTH, HEIGHT = 640, 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

sys.stdout = file("stdout.txt", "w")
sys.stderr = file("stderr.txt", "w")

BLACK = (0,0,0)

def move(d, v, m):
    d = d + v
    if d > m:
        d = m
        v = -v
    elif d < 0:
        d = 0
        v = -v
    return d, v


while 1:
    
    lines = []

    Rspeed, Gspeed, Bspeed = random.randrange(-5,6),random.randrange(-5,6),random.randrange(-5,6)
    R, G, B = (random.randrange(256), random.randrange(256), random.randrange(256))

    x, y = random.randrange(WIDTH), random.randrange(HEIGHT)
    xspeed, yspeed = random.randrange(1,2) * random.randrange(-1,2,2), \
                     random.randrange(1,2) * random.randrange(-1,2,2)

    X, Y = random.randrange(WIDTH), random.randrange(HEIGHT)
    Xspeed, Yspeed = random.randrange(1,2) * random.randrange(-1,2,2), \
                     random.randrange(1,2) * random.randrange(-1,2,2)

    for i in range(100):
        
        R, Rspeed = move(R, Rspeed, 255)
        G, Gspeed = move(G, Gspeed, 255)
        B, Bspeed = move(B, Bspeed, 255)
            
        color = (R, G, B)

        # THIS IS THE OLD CODE:
        #line = [x, y, xspeed, yspeed,
        #        X, Y, Xspeed, Yspeed,
        #        color]

        # THIS IS THE NEW CODE:
        line = {}
        line['x'] = x
        line['y'] = y
        line['xspeed'] = xspeed
        line['yspeed'] = yspeed
        line['X'] = X
        line['Y'] = Y
        line['Xspeed'] = Xspeed
        line['Yspeed'] = Yspeed
        line['color'] = color
        
        lines.append(line)

    FRAME_RATE = 1000.0 / 60

    count = 0
    num_lines = 1

    initial_time = pygame.time.get_ticks()
    
    while 1:

        next_initial_time = pygame.time.get_ticks()
        if next_initial_time - initial_time > 60000:
            break

        starttime = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:     
                sys.exit()

        # Move lines in lines[:num_lines]
        for line in lines[:num_lines]:
            # NEW CODE
            line['x'], line['xspeed'] = move(line['x'], line['xspeed'], WIDTH - 1)
            line['y'], line['yspeed'] = move(line['y'], line['yspeed'], HEIGHT - 1)
            line['X'], line['Xspeed'] = move(line['X'], line['Xspeed'], WIDTH - 1)
            line['Y'], line['Yspeed'] = move(line['Y'], line['Yspeed'], HEIGHT - 1)
        
        surface.fill(BLACK)

        # Draw lines in lines[:num_lines]
        for line in lines[:num_lines]:
            # NEW CODE
            pygame.draw.line(surface, line['color'], (line['x'],line['y']), (line['X'],line['Y']))
        
        pygame.display.flip()

        if num_lines < 100:
            count = count + 1

        if count >= 10:
            if num_lines < 100:
                num_lines = num_lines + 1
                count = 0

        endtime = pygame.time.get_ticks()
        totaltime = starttime - endtime
        timeleft = int(FRAME_RATE - totaltime)
        if timeleft > 0:
            pygame.time.delay(timeleft)
