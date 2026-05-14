import sys, pygame

pygame.init()
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)

while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x = input("x: ")
    y = input("y: ")
    r = input("r: ")

    pygame.draw.circle(surface, (255, 0, 0), [x, y], r, 0)
    
    # Draw surface
    surface.blit(alien, alienrect)
    pygame.display.flip()
