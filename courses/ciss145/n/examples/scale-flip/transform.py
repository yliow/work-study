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


font = pygame.font.Font(None, 60)
image = font.render("CS Spring 2009 Presentations", True, WHITE)

angle = 0
dangle = 360
scale = 1
dscale = 0

rect = image.get_rect()
oldw = rect.w
w = rect.w
h = rect.h
dw = -3

while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    oldcenter = rect.center
    w += dw
    if w < 0 or w > oldw:
        if w < 0:
            w = 0
            image = pygame.transform.flip(image, True, False)
        else: w = oldw
        dw = -dw
        
    image2 = pygame.transform.scale(image, (w,h))
    rect2 = image2.get_rect()
    rect2.center = oldcenter

    # Draw surface
    surface.fill(BLACK)
    rect2.center = (WIDTH/2, HEIGHT/2)
    surface.blit(image2, rect2)
    pygame.display.flip()

    pygame.time.delay(5)
