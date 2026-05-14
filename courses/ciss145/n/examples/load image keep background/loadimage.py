import sys, pygame
sys.stderr = file("stderr.txt", "w")
pygame.init()

surface = pygame.display.set_mode((640, 480))
BLACK = (0, 0, 0)

image = pygame.image.load("a.gif")
rect = image.get_rect()
image2 = pygame.Surface((40, 20))
image2.blit(image, rect.move([12, 3]))
image2.set_colorkey(BLACK)

surface.fill(BLACK)
pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(10, 0, 2, 100))
pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(15, 0, 2, 100))
pygame.draw.rect(surface, (0, 0, 255), pygame.Rect(20, 0, 2, 100))
surface.blit(image2, image2.get_rect())
pygame.display.flip()

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.time.delay(100)
