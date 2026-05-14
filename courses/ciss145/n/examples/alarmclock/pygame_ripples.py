import time

def run():

    import sys, pygame

    pygame.init()

    #sys.stdout = file("stdout.txt","w")
    #sys.stderr = file("stderr.txt","w")

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

    start = pygame.time.get_ticks()

    font = pygame.font.Font(None, 100)

    surface.fill((0,0,0))
    display.flip()

    stop = False
    

    target = (11, 7, 0)
    target = target[0] * 3600 + target[1] * 60 + target[0]
    
    print "time"
    stop = False
    while 1:
        
        time0 = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                print event, event.unicode, event.mod
                if event.unicode == ' ': stop = True
                
        if stop: break
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_SPACE]:
            print "break using keypress ..."
            break
        if keypress[pygame.K_F4] and (keypress[pygame.K_RALT] or keypress[pygame.K_LALT]):
            print "break using keypress ..."
            break

        
        surface.fill((0,0,0))
        hour, minute, second = time.localtime()[3:6]
        second = hour * 3600 + minute * 60 + second
        left = target - second
        h = str(left /3600).zfill(2)
        m = str((left  - left/3600) / 60).zfill(2)
        s = str(left % 60).zfill(2)
        strtime0 = '%s:%s:%s' % (h,m,s)
        image = font.render(strtime0, 1, (255, 0, 0))
        imagerect = image.get_rect()
        surface.blit(image, imagerect)
        display.flip()

        pygame.time.delay(200)

    while 1:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

run()
