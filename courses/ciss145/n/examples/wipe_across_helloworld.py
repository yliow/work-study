import pygame, sys
pygame.init()

WIDTH, HEIGHT = 640, 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

WHITE = (255, 255, 255)

font = pygame.font.Font(None, 100)
image = font.render("hello world", 1, WHITE)
rect = image.get_rect()

surface_rect = rect.move((WIDTH - rect.w)/2, (HEIGHT - rect.h)/2)
image_rect = pygame.Rect(0, 0, 0, rect.h)

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()

    # If portion of image to blit is not the full image rect
    # expand it.
    if image_rect.w < rect.w:
        image_rect.w = image_rect.w + 1
        surface.blit(image, surface_rect, image_rect)
    
    pygame.display.flip()
    pygame.time.delay(10)
