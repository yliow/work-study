import sys, pygame

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
print alienrect

# Load sound
tag = pygame.mixer.Sound("ChatTag.wav")

while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move alien
    alienrect = alienrect.move(speed)
    print alienrect

    # Deflect along left and right walls
    if alienrect.left < 0 or alienrect.right > WIDTH:
        print "left or right collision", alienrect.left, alienrect.right
        speed[0] = -speed[0]
        tag.play()

    # Deflect along top and bottom walls
    if alienrect.top < 0 or alienrect.bottom > HEIGHT:
        print "top or bottom collision", alienrect.top, alienrect.bottom
        speed[1] = -speed[1]
        tag.play()

    # Draw surface
    surface.fill(BLACK)
    surface.blit(alien, alienrect)
    pygame.display.flip()

    pygame.time.delay(10)
