import sys, pygame

pygame.init()

sys.stdout = file("stdout.txt","w")
sys.stderr = file("stderr.txt","w")

display = pygame.display
SIZE = WIDTH,HEIGHT = 640,460
surface = display.set_mode(SIZE)

BLACK = (0,0,0)
BACKGROUND = BLACK
surface.fill(BACKGROUND)
display.flip()

from random import seed, randrange
seed()
#p0 = [WIDTH/2,HEIGHT/2]
p0 = [50,50]
color = [255,255,255]

def inc(x,dx,max,topdecay=1,bottomdecay=1):
    x += dx
    if x > max:
        x = 2*max - x
        dx = -dx*topdecay
    elif x < 0:
        x = -x
        dx = -dx*bottomdecay
    return x,dx

def inc_gravity(y,dy,max):
    # scale: 1 pixel = 1 mm use 9.82/1000
    # scale: 1 pixel = 1 cm use 9.82/100
    dt = 1000/30
    dy += 9.82 /1000 * 1000/30
    return inc(y,dy,max,topdecay=0.75)

def randcolor():
    def r(): return 128 + randrange(0,128)
    return [r(),r(),r()]

def randvelocity():
    return [randrange(4,7), randrange(-5,2)]

loop_count = 0
points = []
tpoints = []
MAX_POINTS = 2000
for i in range(MAX_POINTS):
    p = p0[:]
    v = randvelocity()
    color = randcolor()
    tpoints.append( [p,v,color[:]] )

more_points = True

frame_rate = 1000/30

while 1:
    time0 = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # add object
    if more_points:
        loop_count += 1
        if loop_count==1:
            loop_count = 0
            points.append( tpoints[0] )
            tpoints.remove( tpoints[0] )
            more_points = len(points)<MAX_POINTS
        
    # erase, move, draw
    surface.lock()
    for [p,v,color] in points:
        # erase
        surface.fill(BACKGROUND, [p[0],p[1],1,1])
        # move
        p[0],v[0] = inc(p[0],v[0],WIDTH,topdecay=0.75,bottomdecay=0.75)
        p[1],v[1] = inc_gravity(p[1],v[1],HEIGHT)
        # draw
        surface.fill(color, [p[0],p[1],1,1])
    surface.unlock()
    display.flip()
    
    dtime = frame_rate - (pygame.time.get_ticks() - time0)
    if dtime > 0:
        pygame.time.delay(dtime)
