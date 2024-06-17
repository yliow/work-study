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

NUM_ALIENS = 50

# Computer speeds 
speeds = []
for i in range(NUM_ALIENS):
    XSPEED = random.randrange(-3, 3)
    YSPEED = random.randrange(-3, 3)
    speed = [XSPEED, YSPEED]
    speeds.append(speed)

# Load alien image
alien = pygame.image.load("GalaxianAquaAlien.gif")

# Construct alienrects
alienrects = []
for i in range(NUM_ALIENS):
    alienrect = alien.get_rect()
    alienrect = alienrect.move([random.randrange(600), random.randrange(400)])
    alienrects.append(alienrect)

# Load sound
tag = pygame.mixer.Sound("ChatTag.wav")

while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for i in range(NUM_ALIENS):
        
        # Move alien
        alienrects[i] = alienrects[i].move(speeds[i])

        # Deflect along left and right walls
        if alienrects[i].left < 0 or alienrects[i].right > WIDTH:
            speeds[i][0] = -speeds[i][0]
            tag.play()

        # Deflect along top and bottom walls
        if alienrects[i].top < 0 or alienrects[i].bottom > HEIGHT:
            speeds[i][1] = -speeds[i][1]
            tag.play()

    # Draw surface
    surface.fill(BLACK)

    for i in range(NUM_ALIENS):
        surface.blit(alien, alienrects[i])
        
    pygame.display.flip()
