def run():

    import sys, pygame

    pygame.init()

    sys.stdout = open("stdout.txt","w")
    sys.stderr = open("stderr.txt","w")

    display = pygame.display
    size = w,h = 640,460
    surface = display.set_mode(size)

    black = (0,0,0)
    surface.fill(black)
    display.flip()

    from random import seed, randrange
    seed()
    p0 = [20,20]
    black = [0,0,0]
    color = [255,255,255]
    radius = 6

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
        dt = 1000 // 30
        dy += 9.82 // 1000 * 1000 // 30
        return inc(y,dy,max,topdecay=0.5)

    loop_count = 0
    points = []
    tpoints = []
    MAX_POINTS = 100
    for i in range(MAX_POINTS):
        p = p0[:]
        v = [randrange(4,5), randrange(0,3)-2]
        color = [128+randrange(0,128),128+randrange(0,128),128+randrange(0,128)]
        tpoints.append( [p,v,color[:]] )
    tpoints = []
    more_points = True

    frame_rate = 1000 // 30

    #surface.lock()
    p = [w // 2, h // 2]
    objects = []
    tobjects = []
    MAX_OBJECTS = 5
    for i in range(MAX_OBJECTS):
        color = [255, 255, 255]
        tobjects.append([color, p, 1, 1])
    pygame.display.flip()
    more_objects = True

    v = 1
    while 1:
        loop_count += 1
        time0 = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # move object
        surface.lock()
        for object in  objects:
            [color,p,radius,t] = object
            pygame.draw.circle(surface, black, p, radius, t)
            radius,v = inc(radius,v,w-radius // 2,topdecay=1,bottomdecay=1)
            #object = [color,p,radius,t]
            object[2] = radius
            object[0] = [int(color[0]/1.1),int(color[0]/1.1),int(color[0]/1.1)]
            #p[0],v[0] = inc(p[0],v[0],w-radius/2,topdecay=0.5,bottomdecay=0.5)
            #p[1],v[1] = inc_gravity(p[1],v[1],h-radius/2)
        surface.unlock()

        # add object
        if more_objects and loop_count==10:
            loop_count = 0
            objects.append( tobjects[0] )
            tobjects.remove( tobjects[0] )
            more_objects = len(tobjects)>0
        
        # draw object
        surface.lock()
        for [color,p,radius,t] in objects:
            #surface.fill(color, [p[0],p[1],1,1]) # point
            pygame.draw.circle(surface, color, p, radius, t) # circle
        surface.unlock()
        
        display.flip()

        dtime = frame_rate - (pygame.time.get_ticks() - time0)
        if dtime > 0:
            pygame.time.delay(dtime)




run()
