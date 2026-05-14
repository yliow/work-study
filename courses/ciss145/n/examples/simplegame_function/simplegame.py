import pygame, sys, random
pygame.init()
random.seed()

# Create alien
def get_alien():
    alien = {}
    alien["image"] = pygame.image.load("GalaxianAquaAlien.gif")
    alien["rect"] = alien["image"].get_rect()
    alien["rect"] = alien["rect"].move([0,SCORE_HEIGHT])
    alien["speed"] = [1, 0]
    return alien

ALIEN_Y_INCREMENT = 10

# Create flagship
def get_ship():
    ship = {}
    ship["image"] = pygame.image.load("GalaxianGalaxip.gif")
    ship["rect"] = ship["image"].get_rect()
    x = (WIDTH - ship["rect"].w) / 2
    y = HEIGHT - ship["rect"].h
    ship["rect"] = ship["rect"].move([x,y])
    ship["speed"] = [0, 0]
    return ship

# Ship's laser
def get_laser():
    laser = {}
    laser["rect"] = pygame.Rect(0, 0, 4, 8)
    laser["speed"] = [0, 0]
    laser["alive"] = False
    laser["sound"] = pygame.mixer.Sound("laser.wav")
    return laser

# Explosion sound
def get_explosion():
    explosion = {}
    explosion["sound"] = pygame.mixer.Sound("gexplode.wav")
    explosion["played"] = False
    return explosion

def move(d, v, m):
    d = d + v
    if d < 0:
        d = 0
        v = -v
    elif d > m:
        d = m
        v = -v
    return d, v

WIDTH, HEIGHT = 640, 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

pygame.key.set_repeat(10, 10)

SCORE_HEIGHT = 24
BLACK = (0, 0, 0)
RED = (255, 0, 0)
sys.stdout = file("stdout.txt", "w")
sys.stderr = file("stderr.txt", "w")

alien = get_alien()
ship = get_ship()
laser = get_laser()
explosion = get_explosion()

collides = False
while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keypress = pygame.key.get_pressed()
            if keypress[pygame.K_LEFT]:
                ship["speed"] = [-1, 0]
            if keypress[pygame.K_RIGHT]:
                ship["speed"] = [1, 0]
            if keypress[pygame.K_SPACE]:
                if not laser["alive"]:
                    laser["alive"] = True
                    laser["speed"] = [0, -2]
                    laser["rect"].x = ship["rect"].x + (ship["rect"].w - laser["rect"].w)/2
                    laser["rect"].y = ship["rect"].y - laser["rect"].w
                    laser["sound"].play()

    surface.fill(BLACK)

    if not collides:
        alien["rect"].x, alien["speed"][0] = move(alien["rect"].x, alien["speed"][0], WIDTH - alien["rect"].w)
        if random.randrange(100) == 0:
            alien["rect"].y = alien["rect"].y + ALIEN_Y_INCREMENT

        ship["rect"].x, ship["speed"][0] = move(ship["rect"].x, ship["speed"][0], WIDTH - ship["rect"].w)
        ship["speed"] = [0, 0]

        if laser["alive"]:
            laser["rect"].y, laser["speed"][1] = move(laser["rect"].y, laser["speed"][1], HEIGHT - laser["rect"].h)
            if laser["rect"].y < SCORE_HEIGHT:
                laser["alive"] = False

    collides = alien["rect"].colliderect(ship["rect"]) or laser["rect"].colliderect(alien["rect"])

    if collides == True and explosion["played"] == False:
        explosion["sound"].play()
        explosion["played"] = True
        pygame.time.delay(100)
                
    surface.blit(alien["image"], alien["rect"])
    surface.blit(ship["image"], ship["rect"])
    if laser["alive"]:
        pygame.draw.rect(surface, RED, laser["rect"])
    pygame.display.flip()

    # Display message is there is a collision and then break
    if collides == True:
        if alien["rect"].colliderect(ship["rect"]):
            message = "The alien had you for lunch"
            score = 0
        else:
            message = "You saved the world!"
            score = 500 - alien["rect"].y

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
    
