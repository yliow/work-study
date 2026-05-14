import sys, pygame, random
random.seed()

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
RED = (255, 0, 0)
STATUS_BAR_HEIGHT = 0

explosion_sound = pygame.mixer.Sound("explosion.wav")


pygame.mixer.music.load("Play_That_Funky_Music.mid")
pygame.mixer.music.play(-1)


# Score
score_font = pygame.font.Font(None, 50)
score = 0

# My ship's data
myship = pygame.image.load("GalaxianGalaxip.gif")
myship_rect = myship.get_rect()
x = (WIDTH - myship_rect.w)/2
y = HEIGHT - myship_rect.h - STATUS_BAR_HEIGHT
myship_rect = myship_rect.move([x,y])

# Text
font = pygame.font.Font(None, 50)
WHITE = (255, 255, 255)
game_title_image = font.render("Galaxian 0.0.1", 1, WHITE)
game_title_rect = game_title_image.get_rect()
game_title_rect = game_title_rect.move([100, 200])

# Flagship
flagship = pygame.image.load("GalaxianFlagship.gif")
flagship_rect = flagship.get_rect()
flagship_rect = flagship_rect.move([300, 100])
flagship_rect0 = flagship.get_rect()
flagship_rect0 = flagship_rect0.move([300, 100])
flagship_speed = 4
MOVE_LEFT = 0
MOVE_RIGHT = 1
ATTACK = 2
REJOIN = 3
  
flagship_state = MOVE_LEFT

# Alien's data
alien = pygame.image.load("GalaxianAquaAlien.gif")
alien_rects = []
aliens_isalive = []
MAX_ALIENS = 50
for i in range(MAX_ALIENS):
    alien_rect = alien.get_rect()
    x = random.randrange(600)
    y = random.randrange(300) 
    alien_rect = alien_rect.move([x, y])
    alien_rects.append(alien_rect)
    aliens_isalive.append(True)

# Laser's data
MAX_LASERS = 40
laser_rects = []
lasers_isalive = []
for i in range(MAX_LASERS):
    laser_rect = pygame.Rect(0,0,2,8)
    laser_rects.append(laser_rect)
    lasers_isalive.append(False)

laser_speed = 16
laser_sound = pygame.mixer.Sound("laser.wav")


while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Process inputs
    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_LEFT]:
        myship_rect = myship_rect.move([-8, 0])
        if myship_rect.x < 0:
            myship_rect.x = 0
    if keypressed[pygame.K_RIGHT]:
        myship_rect = myship_rect.move([8, 0])
        if myship_rect.right > 639:
            myship_rect.right = 639
    if keypressed[pygame.K_UP]:
        myship_rect = myship_rect.move([0, -8])
        #if myship_rect.right > 639:
        #    myship_rect.right = 639
    if keypressed[pygame.K_DOWN]:
        myship_rect = myship_rect.move([0, 8])
        #if myship_rect.right > 639:
        #    myship_rect.right = 639

    if keypressed[pygame.K_SPACE]:
        for i in range(MAX_LASERS):        
            if not lasers_isalive[i]:
                lasers_isalive[i] = True
                laser_rects[i].x = myship_rect.x + (myship_rect.w - laser_rects[i].w) / 2
                laser_rects[i].y = myship_rect.y - laser_rects[i].h
                laser_sound.play()
                break
            
    # Objects move
    for i in range(MAX_LASERS):
        if lasers_isalive[i]:
            laser_rects[i].y = laser_rects[i].y - laser_speed

    for i in range(MAX_ALIENS):
        alien_rects[i].x = alien_rects[i].x + random.randrange(-2,3)

    # Move flagship
    if flagship_state == MOVE_LEFT:
        flagship_rect = flagship_rect.move([-flagship_speed,0])
        if flagship_rect.left < 0:
            flagship_rect.left = 0
            flagship_state = MOVE_RIGHT
        if random.randrange(100) < 1:
            flagship_state = ATTACK
    elif flagship_state == MOVE_RIGHT:
        flagship_rect = flagship_rect.move([flagship_speed,0])
        if flagship_rect.right > WIDTH - 1:
            flagship_rect.right = WIDTH - 1
            flagship_state = MOVE_LEFT
        if random.randrange(100) < 10:
            flagship_state = ATTACK
    elif flagship_state == ATTACK:
        flagship_rect = flagship_rect.move([0,flagship_speed])
        if flagship_rect.x < myship_rect.x:
            flagship_rect.x = flagship_rect.x + flagship_speed
        elif flagship_rect.x > myship_rect.x:
            flagship_rect.x = flagship_rect.x - flagship_speed
        if flagship_rect.top >= HEIGHT:
            flagship_state = REJOIN
            flagship_rect.bottom = 0
            flagship_rect.left = 100
    elif flagship_state == REJOIN:
        if flagship_rect.x < flagship_rect0.x:
            flagship_rect.x = flagship_rect.x + 1
        elif flagship_rect.x > flagship_rect0.x:
            flagship_rect.x = flagship_rect.x - 1
        if flagship_rect.y > flagship_rect0.y:
            flagship_rect.y = flagship_rect.y - 1
        elif flagship_rect.y < flagship_rect0.y:
            flagship_rect.y = flagship_rect.y + 1
        if flagship_rect.x == flagship_rect0.x and flagship_rect.y == flagship_rect0.y:
            flagship_state = MOVE_RIGHT

    # Collision
    for i in range(MAX_LASERS):
        if lasers_isalive[i]:
            for j in range(MAX_ALIENS):
                if aliens_isalive[j] and alien_rects[j].colliderect(laser_rects[i]):
                    lasers_isalive[i] = False
                    aliens_isalive[j] = False
                    score = score + 10
                    explosion_sound.play()

    # Collision with top of window
    for i in range(MAX_LASERS):
        if lasers_isalive[i] and laser_rects[i].y <= 0:
            lasers_isalive[i] = False
    
    # Drawing part
    surface.fill(BLACK)

    surface.blit(game_title_image, game_title_rect)

    # draw score
    score_image = score_font.render(str(score), 1, WHITE)
    score_rect = score_image.get_rect()
    score_rect = score_rect.move([550, 0])
    surface.blit(score_image, score_rect)
    
    surface.blit(myship, myship_rect)

    for i in range(MAX_ALIENS):
        if aliens_isalive[i]:
            surface.blit(alien, alien_rects[i])

    pygame.draw.rect(surface, (0,255,0), flagship_rect0)             
    surface.blit(flagship, flagship_rect)

    for i in range(MAX_LASERS):
        if lasers_isalive[i]:
            pygame.draw.rect(surface, RED, laser_rects[i])
        
    pygame.display.flip()
    pygame.time.delay(100)
    

    
