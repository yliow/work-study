import sys, pygame
import random
# Initialize Pygame
pygame.init()
random.seed()

# Set surface to 680x480
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Hello world!')
icon = pygame.image.load("a.bmp")
pygame.display.set_icon(icon)

while 1:
    x0 = random.randrange(640)
    y0 = random.randrange(480)
    x1 = random.randrange(20)
    y1 = random.randrange(480)
    R = random.randrange(256)
    G = random.randrange(256)
    B = random.randrange(256)
    pygame.draw.circle(surface, (R,G,B), (x0,y0), x1)
    pygame.display.flip()
    
"""
BLACK = (0, 0, 0)

# Set speed of alien to [1,2]
XSPEED = 1
YSPEED = 2
speed = [XSPEED, YSPEED]

# Load alien image and get image rect
alien = pygame.image.load("GalaxianAquaAlien.gif")
alienrect = alien.get_rect()

# Load sound
tag = pygame.mixer.Sound("ChatTag.wav")

while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move alien
    alienrect = alienrect.move(speed)

    # Deflect along left and right walls
    if alienrect.left < 0 or alienrect.right > WIDTH:
        speed[0] = -speed[0]
        tag.play()

    # Deflect along top and bottom walls
    if alienrect.top < 0 or alienrect.bottom > HEIGHT:
        speed[1] = -speed[1]
        tag.play()

    # Draw surface
    surface.fill(BLACK)
    surface.blit(alien, alienrect)
    pygame.display.flip()
"""
