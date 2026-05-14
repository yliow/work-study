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


font = pygame.font.Font(None, 48)
image = font.render("h", True, WHITE)
rect = image.get_rect()
xs = [((255, 255, 255), image, rect)]


while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    

    # Draw surface
    surface.fill(BLACK)
    surface.blit(image2, rect2)
    pygame.display.flip()

    pygame.time.delay(5)
