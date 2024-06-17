import sys, pygame
sys.stdout = file('stdout.txt', 'w')
sys.stderr = file('stderr.txt', 'w')

pygame.init()

# Set surface to 680x480
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

image = pygame.image.load("GalaxianFlagship.gif")
rect = image.get_rect()
image2 = pygame.Surface((rect.w * 2, rect.h * 2))
image2.blit(image, rect)
image = image2

angle = 0
dangle = 1

rect = pygame.Rect((0, 0, 640, 480))

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    oldcenter = rect.center
    image2 = pygame.transform.rotate(image, angle)
    angle += dangle
    rect2 = image2.get_rect()
    rect2.center = oldcenter

    # Draw surface
    surface.fill(BLACK)
    surface.blit(image2, rect2)
    pygame.display.flip()

    pygame.time.delay(5)
