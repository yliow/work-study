# file: simplygalaxian.py

import pygame, sys, random
pygame.init()
random.seed()

from CONSTANTS import *
from util import *
import Alien, Ship, Laser, Explosion

surface = pygame.display.set_mode(SIZE)

pygame.key.set_repeat(10, 10)

sys.stdout = file("stdout.txt", "w")
sys.stderr = file("stderr.txt", "w")

alien = Alien.get_alien()
ship = Ship.get_ship()
laser = Laser.get_laser()
explosion = Explosion.get_explosion()

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
        alien = Alien.move_alien(alien)
        ship = Ship.move_ship(ship)
        laser = Laser.move_laser(laser)

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
