import pygame, sys, random
pygame.init()
random.seed()

WIDTH, HEIGHT = 640, 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

WHITE = (255, 255, 255)

font = pygame.font.Font(None, 100)
image = font.render("hello world", 1, WHITE)
rect = image.get_rect()

xoffset = (WIDTH - rect.w) / 2
yoffset = (HEIGHT - rect.h) / 2

count = 0
size = 1

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()

    count = count + 1
    if count % 10000 == 0:
        size = size + 1
        
    x = random.randrange(rect.w)
    y = random.randrange(rect.h)
    image_rect = pygame.Rect(x, y, size, size)
    surface_rect = rect.move(xoffset + x, yoffset + y)
    surface.blit(image, surface_rect, image_rect)

    pygame.display.flip()
