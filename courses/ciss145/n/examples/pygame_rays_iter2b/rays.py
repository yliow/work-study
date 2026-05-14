import pygame, sys
pygame.init()

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

lines = []
for i in range(100):
    line = [50, 60, 2, 1, 10, 200, 1, -1]
    lines.append(line)

FRAME_RATE = 1000.0 / 60

count = 0
num_lines = 1

while 1:

    starttime = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()

    # Move lines in lines[:num_lines]
    for line in lines[:num_lines]:
        line[0], line[2] = move(line[0], line[2], WIDTH - 1)
        line[1], line[3] = move(line[1], line[3], HEIGHT - 1)
        line[4], line[6] = move(line[4], line[6], WIDTH - 1)
        line[5], line[7] = move(line[5], line[7], HEIGHT - 1)
    
    surface.fill(black)

    # Draw lines in lines[:num_lines]
    for line in lines[:num_lines]:        
        pygame.draw.line(surface, violet, (line[0],line[1]), (line[4],line[5]))
    
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
