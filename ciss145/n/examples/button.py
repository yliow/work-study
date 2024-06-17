import pygame, sys
pygame.init()

WIDTH, HEIGHT = 640, 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# up button
points1 = [(0,0),(100,0),(100,50),(95,45),(95,5),(5,5),(0,0)]
points2 = [(0,0),(0,50),(100,50),(95,45),(5,45),(5,5),(0,0)]
color1 = (255,255,255)
color2 = (100,100,100)
color3 = (200,200,200)

# down button
dpoints1 = [(1,1),(101,1),(101,51),(96,46),(96,6),(6,6),(1,1)]
dpoints2 = [(1,1),(1,51),(101,51),(96,46),(6,46),(6,6),(1,1)]
dcolor1 = (255,255,255)
dcolor2 = (100,100,100)
dcolor3 = (200,200,200)

# label button
font = pygame.font.Font(None, 24)
image = font.render("Click me", 1, BLACK)
rect = image.get_rect()
rect = rect.move((100 - rect.w)/2, (50 - rect.h)/2)
drect = rect.move(1,1)

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            surface.fill(BLACK)
            pygame.draw.polygon(surface, dcolor1, dpoints1)
            pygame.draw.polygon(surface, dcolor2, dpoints2)
            pygame.draw.rect(surface, color3, pygame.Rect(6,6,91,41))
            surface.blit(image, drect)
            pygame.display.flip()
            if 0 <= x <= 100 and 0 <= y <= 50:
                print "pressed"
            pygame.time.delay(1000)
            
    surface.fill(BLACK)
    pygame.draw.polygon(surface, color1, points1)
    pygame.draw.polygon(surface, color2, points2)
    pygame.draw.rect(surface, color3, pygame.Rect(5,5,90,40))
    surface.blit(image, rect)

    pygame.display.flip()
    pygame.time.delay(10)
