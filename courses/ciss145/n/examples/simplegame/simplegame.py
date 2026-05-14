import pygame, sys, random
pygame.init()
random.seed()

WIDTH, HEIGHT = 640, 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

pygame.key.set_repeat(1000, 1000)

SCORE_HEIGHT = 24
BLACK = (0, 0, 0)
RED = (255, 0, 0)
sys.stdout = file("stdout.txt", "w")
sys.stderr = file("stderr.txt", "w")

# Create alien
alien_image = pygame.image.load("GalaxianAquaAlien.gif")
alien_rect = alien_image.get_rect()
alien_rect = alien_rect.move([0,SCORE_HEIGHT])
alien_speed = [1, 0]
ALIEN_Y_INCREMENT = 3

# Create flagship
ship_image = pygame.image.load("GalaxianGalaxip.gif")
ship_rect = ship_image.get_rect()
x = (WIDTH - ship_rect.w) / 2
y = HEIGHT - ship_rect.h
ship_rect = ship_rect.move([x,y])
ship_speed = [0, 0]

# Ship's laser
laser_rect = pygame.Rect(0, 0, 5, 10)
laser_speed = [0, 0]
laser_alive = False

# Laser sound
laser_sound = pygame.mixer.Sound("laser.wav")

# Explosion sound
explosion_sound = pygame.mixer.Sound("gexplode.wav")
explosion_played = False
def move(d, v, m):
    d = d + v
    if d < 0:
        d = 0
        v = -v
    elif d > m:
        d = m
        v = -v
    return d, v

collides = False

FR = 1000/60

while 1:
    start = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keypress = pygame.key.get_pressed()
            if keypress[pygame.K_LEFT]:
                ship_speed = [-1, 0]
            if keypress[pygame.K_RIGHT]:
                ship_speed = [1, 0]
            if keypress[pygame.K_SPACE]:
                if not laser_alive:
                    laser_alive = True
                    laser_speed = [0, -2]
                    laser_rect.x = ship_rect.x + (ship_rect.w - laser_rect.w)/2
                    laser_rect.y = ship_rect.y - laser_rect.w
                    laser_sound.play()

    surface.fill(BLACK)

    if not collides:
        alien_rect.x, alien_speed[0] = move(alien_rect.x, alien_speed[0], WIDTH - alien_rect.w)
        if random.randrange(100) == 0:
            alien_rect.y = alien_rect.y + ALIEN_Y_INCREMENT

        ship_rect.x, ship_speed[0] = move(ship_rect.x, ship_speed[0], WIDTH - ship_rect.w)
        ship_speed = [0, 0]

        if laser_alive:
            laser_rect.y, laser_speed[1] = move(laser_rect.y, laser_speed[1], HEIGHT - laser_rect.h)
            if laser_rect.y < SCORE_HEIGHT:
                laser_alive = False

    collides = alien_rect.colliderect(ship_rect) or laser_rect.colliderect(alien_rect)

    if collides == True and explosion_played == False:
        explosion_sound.play()
        explosion_played = True
        pygame.time.delay(100)
                
    surface.blit(alien_image, alien_rect)
    surface.blit(ship_image, ship_rect)
    if laser_alive:
        pygame.draw.rect(surface, RED, laser_rect)
    pygame.display.flip()

    # Display message is there is a collision and then break
    if collides == True:
        if alien_rect.colliderect(ship_rect):
            message = "The alien had you for lunch"
            score = 0
        else:
            message = "You saved the world!"
            score = 500 - alien_rect.y

        # Draw the score
        WHITE = (255, 255, 255)
        font = pygame.font.Font(None, SCORE_HEIGHT)
        image = font.render("Score: " + str(score), 1, WHITE)
        rect = image.get_rect()
        surface.blit(image, rect)

        # Draw a message
        font = pygame.font.Font(None, 48)
        image = font.render(message, 1, WHITE)
        rect = image.get_rect()
        surface_rect = rect.move((WIDTH - rect.w)/2, (HEIGHT - rect.h)/2)
        image_rect = pygame.Rect(0, 0, 0, rect.h)

        while 1:
            if image_rect.w < rect.w:
                image_rect.w = image_rect.w + 1
                surface.blit(image, surface_rect, image_rect)
            else:
                break
            pygame.display.flip()
            pygame.time.delay(10)
        pygame.time.delay(3000)
        break

    end = pygame.time.get_ticks()
    dt = end - start
    if (dt > 0):
        pygame.time.delay(dt)
    
