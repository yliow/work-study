def main():

    import sys, pygame, random
    random.seed()

    # Initialize Pygame
    pygame.init()

    # Set surface to 680x480    
    WIDTH = 640
    HEIGHT = 480
    SIZE = (WIDTH, HEIGHT)
    surface = pygame.display.set_mode(SIZE)
    BLACK = (0, 0, 0)

    # Set speed of alien to [1,2]
    XSPEED = 1
    YSPEED = 2
    speed = [XSPEED, YSPEED]

    # Load alien image and get image rect
    alien = pygame.image.load("GalaxianAquaAlien.gif")
    alienrect = alien.get_rect()

    initial_pos = [random.randrange(600), random.randrange(400)]
    initial_speed = [random.randrange(1, 3) * random.randrange(-1, 2, 2),
                     random.randrange(1, 3) * random.randrange(-1, 2, 2)]

    alienrects = []
    speeds = []

    alienrect = alien.get_rect()
    alienrect = alienrect.move(initial_pos)
    speed = initial_speed[:]
    alienrects.append(alienrect)
    speeds.append(speed)
        
    # Load sound
    tag = pygame.mixer.Sound("ChatTag.wav")

    count = 0
    numaliens = random.randrange(5, 16)
    
    while 1:

        # Exit if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        if len(alienrects) < numaliens:
            count = count + 1
            if count == 14:
                count = 0
                alienrect = alien.get_rect()
                alienrect = alienrect.move(initial_pos)
                speed = initial_speed[:]
                alienrects.append(alienrect)
                speeds.append(speed)
        
        # Move alien
        for i in range(len(alienrects)):
            alienrects[i] = alienrects[i].move(speeds[i])

        # Deflect along left and right walls
        for i in range(len(alienrects)):
            if alienrects[i].left < 0 or alienrects[i].right > WIDTH:
                speeds[i][0] = -speeds[i][0]
                tag.play()

        # Deflect along top and bottom walls
        for i in range(len(alienrects)):
            if alienrects[i].top < 0 or alienrects[i].bottom > HEIGHT:
                speeds[i][1] = -speeds[i][1]
                tag.play()

        # Draw surface
        surface.fill(BLACK)
        for i in range(len(alienrects)):
            surface.blit(alien, alienrects[i])
        pygame.display.flip()

        pygame.time.delay(500)
