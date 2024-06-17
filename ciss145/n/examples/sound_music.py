import pygame, sys
pygame.init()

sys.stdout = file("stdout.txt", "w")
sys.stderr = file("stderr.txt", "w")

WIDTH, HEIGHT = 640, 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)

sound1 = pygame.mixer.Sound("gameover.wav")
sound2 = pygame.mixer.Sound("start.wav")

pygame.mixer.music.load("demo.mid")

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:     
            sys.exit()

        if event.type == pygame.KEYDOWN:
            keypressed = pygame.key.get_pressed()
            if keypressed[pygame.K_LEFT]:
                pygame.mixer.music.play(-1)
            if keypressed[pygame.K_RIGHT]:
                pygame.mixer.music.stop()
