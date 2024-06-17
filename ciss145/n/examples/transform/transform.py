import sys, pygame
sys.stdout = file('stdout.txt', 'w')
sys.stderr = file('stderr.txt', 'w')

# Initialize Pygame
pygame.init()

# Set surface to 680x480
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


font = pygame.font.Font(None, 72)
image = font.render("hello world", True, WHITE)


# Load alien image and get image rect
'''
image = pygame.image.load("GalaxianFlagship.gif")
rect = image.get_rect()
surface.blit(image, rect)
pygame.display.flip()
'''

angle = 0
dangle = 360
scale = 1
dscale = 0

#surf = pygame.Surface((640, 480))
rect = pygame.Rect((0, 0, 640, 480))
#pygame.draw.rect(surf, (255,0,0), rect)

while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move alien
    oldcenter = rect.center
    #image2 = pygame.transform.rotate(image, angle)
    image2 = pygame.transform.rotozoom(image, angle, scale)
    angle += dangle
    scale -= dscale
    if scale < 0.001 or scale > 10:
        dscale = -dscale
    rect2 = image2.get_rect()
    rect2.center = oldcenter

    # Draw surface
    surface.fill(BLACK)
    surface.blit(image2, rect2)
    pygame.display.flip()

    pygame.time.delay(5)
