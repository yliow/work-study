class vec2d:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)
    def __str__(self):
        return "vec2d(%s, %s)" % (self.x, self.y)
    def __iadd__(self, v):
        self.x += v.x
        self.y += v.y
        return self
    def __add__(self, v):
        ret = vec2d(self.x, self.y)
        ret += v
        return ret
    def __imul__(self, c):
        c = float(c)
        self.x *= c
        self.y *= c
        return self
    def __mul__(self, c):
        c = float(c)
        ret = vec2d(self.x, self.y)
        ret *= c
        return ret
    def __rmul__(self, c):
        return self * c
    def __div__(self, c):
        return self * (1.0/c)
    def __idiv__(self, c):
        self *= (1.0 / c)
        return self
    

class Block:
    def __init__(self, m, p, v):
        self.m = float(m)
        self.p = p 
        self.v = v
        # self.a = a
    def update(self, force=vec2d(0,0), torque=0.0, dt=0.01):
        a = force * (1.0/self.m)
        self.v += a
        self.p += self.v
        
import sys; sys.exit()

def run():
    
    import sys, pygame

    pygame.init()

    sys.stdout = file("stdout.txt","w")
    sys.stderr = file("stderr.txt","w")

    display = pygame.display
    w,h = 640,460
    size = (w,h)
    surface = display.set_mode(size)

    BLACK = (0,0,0)
    surface.fill(BLACK)
    display.flip()

    from random import seed, randrange
    seed()
    p0 = [20,20]
    BLACK = [0,0,0]
    color = [255,255,255]

    
    frame_rate = 1000/30

    while 1:
        time0 = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # recompute blocks position

        # draw object
        surface.lock()
        # pygame.draw.polygon(surface, WHITE, points)
        surface.unlock()
        
        display.flip()
        
        dtime = frame_rate - (pygame.time.get_ticks() - time0)
        if dtime > 0:
            pygame.time.delay(dtime)
