def run():

    import sys, pygame

    pygame.init()

    #sys.stdout = file("stdout.txt","w")
    #sys.stderr = file("stderr.txt","w")

    display = pygame.display
    size = w,h = 800,460
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
    image = font.render("Press space to start", 1, (255, 0, 0))
    imagerect = image.get_rect()
    surface.blit(image, imagerect)
    display.flip()

    print "time"
    stop = False

    tag = pygame.mixer.Sound("ChatTag.wav")
    sound1 = False
    sound2 = False
    soundtime1 = 15 # in seconds
    soundtime2 = 30


    print "press spacebar to start ..."

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_SPACE]:
            break
    
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
        time1 = (time0 - start) * 0.001
        h = str(int(time1 / 3600)).zfill(2)
        m = str(int(time1 / 60) % 60).zfill(2)
        s = str(int(time1) % 60).zfill(2)
        ms = str(int((time1 - int(time1)) * 1000)).zfill(3)
        strtime0 = '%s:%s:%s' % (h,m,s)
        image = font.render(strtime0, 1, (255, 0, 0))
        imagerect = image.get_rect()
        surface.blit(image, imagerect)
        display.flip()

        time1 = (time0 - start) * 0.001
        if not sound1 and time1 >= soundtime1:
            for i in range(5):
                tag.play(); pygame.time.delay(500)
            sound1 = True
        if sound1 and not sound2 and time1 >= soundtime2:
            for i in range(5):
                tag.play(); pygame.time.delay(500)
            sound2 = True
            
        pygame.time.delay(200)

    while 1:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

run()
