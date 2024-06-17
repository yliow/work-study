import sys, pygame, random
pygame.init()

SOUND = True
def demo():
    if not SOUND: return
    #pygame.mixer.music.load("sounds/demo.mid")
    pygame.mixer.music.load("sounds/gameplay.mid")
    pygame.mixer.music.play(-1)

def stop():
    if not SOUND: return
    pygame.mixer.music.stop()
    
startsound = pygame.mixer.Sound("sounds/start.wav")
def start():
    if not SOUND: return
    startsound.play()

gameoversound = pygame.mixer.Sound("sounds/gameover.wav")
def gameover():
    if not SOUND: return
    gameoversound.play()

def gameplay():
    if not SOUND: return
    pygame.mixer.music.load("sounds/gameplay.mid")
    pygame.mixer.music.play()
