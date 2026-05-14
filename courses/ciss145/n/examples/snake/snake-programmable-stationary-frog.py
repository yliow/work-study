import sys, pygame, random
random.seed()
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (600,250)
pygame.init()
#sys.stdout = file('stdout.txt', 'w')
#sys.stderr = file('stderr.txt', 'w')

print "The Robot Snake program is ..."
f = file('program.txt', 'r')
lines = []
for i, line in enumerate(f.readlines()):
    line = line.strip()
    line = line.lower()
    if line == '': continue
    print "command", i + 1, "...", line
    lines.append(line)

print
print
print

# Set surface to 680x480
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)

# Set speed of alien to [1,2]
XSPEED = 1
YSPEED = 0
speed = [XSPEED, YSPEED]

SPEED = 10

# Load sound
tag = pygame.mixer.Sound("ChatTag.wav")

# Snake's body
r = 15
c = (155, 155, 0)

body = []
for i in range(10):
    body.append([100 - i * SPEED, 100])
    
direction = 2

score = 0


font = pygame.font.Font(None, 100)

image = font.render(str(score), 1, (255, 0, 0))
imagerect = image.get_rect()
surface.blit(image, imagerect)

frogx = None
frogy = None
frogjumptime = None
frogdjumptime = 2000
frogdir = random.randrange(4)

starttime = int(pygame.time.get_ticks()) 
timeleft = starttime + 100000

lineno = 0

def move_right():
    speed = [SPEED, 0]
    direction = 2
    move = True
    return speed, direction, move

def move_left():
    speed = [-SPEED, 0]
    direction = 3
    move = True
    return speed, direction, move

def move_up():
    speed = [0, -SPEED]
    direction = 0
    move = True
    return speed, direction, move

def move_down():
    speed = [0, SPEED]
    direction = 1
    move = True
    return speed, direction, move

def do_command(command):
    if command == 'move left':
        return move_left()
    elif command == 'move right':
        return move_right()
    elif command == 'move up':
        return move_up()
    elif command == 'move down':
        return move_down()
    print "I do not understand the command", command
    raise ValueError

def frog_right(frogx, frogy, body):
    return frogx > body[0][0]

def frog_left(frogx, frogy, body):
    return frogx < body[0][0]

def frog_up(frogx, frogy, body):
    return frogy < body[0][1]

def frog_down(frogx, frogy, body):
    return frogy > body[0][1]

def get_boolean(condition, frogx, frogy, body):
    if condition == "if frog is above":
        return frog_up(frogx, frogy, body)
    elif condition == 'if frog is below':
        return frog_down(frogx, frogy, body)
    elif condition == 'if frog is on the right':
        return frog_right(frogx, frogy, body)
    elif condition == 'if frog is on the left':
        return frog_left(frogx, frogy, body)
    else:
        print "I do not understand the condition"
    return False

print "Starting the Robot Snake ..."
while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keypress = pygame.key.get_pressed()
    move = False
    speed = [0, 0]

    if lines:
        line, lines = lines[0], lines[1:]
        lineno += 1
        print "Running Snake Robot command", lineno, "...", line

        try:
            condition, command = line.split(',')
        except:
            condition = ''
            command = line

        #print "condition:", condition
        #print "command:", command

        condition = condition.strip()
        command = command.strip()

        if condition == '':
            condition = True
        else:
            condition = get_boolean(condition, frogx, frogy, body)

        if condition:
            try:
                 speed, direction, move = do_command(command)
            except:
                #print "here"
                pass

        if lines == []:
            print "Snake robot program has ended"
            
    # generate frog
    if frogx == None and random.random() < 0.2:
        frogx = random.randrange(50, WIDTH - 50)
        frogy = random.randrange(50, HEIGHT - 50)
        frogjumptime = pygame.time.get_ticks()
        
    if move:
        x = body[0][0] + speed[0]
        y = body[0][1] + speed[1]
        if r <= x < WIDTH - r and r <= y < HEIGHT - r:
            del body[-1]
            tbody = body[:-1]
            body.insert(0, [x,y])

    # frog jumps
    if frogx != None and (frogjumptime == None or pygame.time.get_ticks() - frogjumptime > frogdjumptime):
        if random.random() < 0.2: frogdir = random.randrange(4)
        newfrogx, newfrogy = frogx, frogy
        if frogdir == 0:
            newfrogy = frogy - 10
        elif frogdir == 1:
            newfrogy = frogy + 10
        elif frogdir == 2:
            newfrogx = frogx + 10
        elif frogdir == 3:
            newfrogx = frogx - 10
            
        if 50 < newfrogx < WIDTH - 50 and 50 < newfrogy < HEIGHT - 50:
            frogx, frogy = newfrogx, newfrogy
            tag.play()
        else:
            frogdir = random.randrange(4)
        frogjumptime = pygame.time.get_ticks()

    # Draw surface
    surface.fill(BLACK)

    # draw frog
    if frogx != None:
        pygame.draw.circle(surface, (0, 255, 0), (frogx, frogy), 10, 0)
        pygame.draw.line(surface, (0, 255, 0), (frogx, frogy), (frogx - 10, frogy - 10), 5)
        pygame.draw.line(surface, (0, 255, 0), (frogx, frogy), (frogx - 10, frogy + 10), 5)
        pygame.draw.line(surface, (0, 255, 0), (frogx, frogy), (frogx + 10, frogy - 10), 5)
        pygame.draw.line(surface, (0, 255, 0), (frogx, frogy), (frogx + 10, frogy + 10), 5)
        if frogdir == 0:
            pygame.draw.circle(surface, (0, 0, 0), (frogx-5, frogy-5), 2, 0)
            pygame.draw.circle(surface, (0, 0, 0), (frogx+5, frogy-5), 2, 0)
        elif frogdir == 1:
            pygame.draw.circle(surface, (0, 0, 0), (frogx-5, frogy+5), 2, 0)
            pygame.draw.circle(surface, (0, 0, 0), (frogx+5, frogy+5), 2, 0)
        elif frogdir == 2:
            pygame.draw.circle(surface, (0, 0, 0), (frogx+5, frogy-5), 2, 0)
            pygame.draw.circle(surface, (0, 0, 0), (frogx+5, frogy+5), 2, 0)
        elif frogdir == 3:
            pygame.draw.circle(surface, (0, 0, 0), (frogx-5, frogy-5), 2, 0)
            pygame.draw.circle(surface, (0, 0, 0), (frogx-5, frogy+5), 2, 0)
            
    for i, t in enumerate(body):
        x,y = t
        if i == 0:
            pygame.draw.circle(surface, c, (x,y), r, 0)
        elif 0 < i < len(body) - 4: 
            pygame.draw.circle(surface, c, (x,y), int(0.8*r), 0)
        elif len(body) - 4 <= i < len(body) - 2:
            pygame.draw.circle(surface, c, (x,y), int(0.7*r), 0)
        elif len(body) - 2 <= i:
            pygame.draw.circle(surface, c, (x,y), int(0.5*r), 0)

    # frog captured
    if frogx != None and (body[0][0] - frogx)**2 + (body[0][1] - frogy)**2 < r*r:
        score += 1
        image = font.render(str(score), 1, (255,0,0))
        imagerect = image.get_rect()
        frogx = frogy = None
        # add circle to body
        lastx, lasty = body[-1]
        secondlastx, secondlasty = body[-2]
        body.append([lastx + lastx - secondlastx, lasty + lasty - secondlasty])
    surface.blit(image, imagerect)
        
    # draw eyes and tongue
    x = body[0][0]
    y = body[0][1]
    if direction == 2 or direction == 3: # traveling left-right
        pygame.draw.circle(surface, (255, 0, 0), (x, y - r/2), 5, 0)
        pygame.draw.circle(surface, (255, 0, 0), (x, y + r/2), 5, 0)
        if direction == 2:
            pygame.draw.line(surface, (255, 0, 0), (x + r, y), (x + 1.5 * r, y), 2)
            pygame.draw.line(surface, (255, 0, 0), (x + 1.5 * r, y), (x + 2 * r, y - 0.5*r), 2)
            pygame.draw.line(surface, (255, 0, 0), (x + 1.5 * r, y), (x + 2 * r, y + 0.5*r), 2)
        else:
            pygame.draw.line(surface, (255, 0, 0), (x - r, y), (x - 1.5 * r, y), 2)
            pygame.draw.line(surface, (255, 0, 0), (x - 1.5 * r, y), (x - 2 * r, y - 0.5*r), 2)
            pygame.draw.line(surface, (255, 0, 0), (x - 1.5 * r, y), (x - 2 * r, y + 0.5*r), 2)
    else:
        pygame.draw.circle(surface, (255, 0, 0), (x - r/2, y), 5, 0)
        pygame.draw.circle(surface, (255, 0, 0), (x + r/2, y), 5, 0)
        if direction == 0:
            pygame.draw.line(surface, (255, 0, 0), (x, y - r), (x, y - 1.5 * r), 2)
            pygame.draw.line(surface, (255, 0, 0), (x, y - 1.5 * r), (x - 0.5 * r, y - 2 * r), 2)
            pygame.draw.line(surface, (255, 0, 0), (x, y - 1.5 * r), (x + 0.5 * r, y - 2 * r), 2)
        else:
            pygame.draw.line(surface, (255, 0, 0), (x, y + r), (x, y + 1.5 * r), 2)
            pygame.draw.line(surface, (255, 0, 0), (x, y + 1.5 * r), (x - 0.5 * r, y + 2 * r), 2)
            pygame.draw.line(surface, (255, 0, 0), (x, y + 1.5 * r), (x + 0.5 * r, y + 2 * r), 2)

    # time left
    now = int(pygame.time.get_ticks())
    timeleft = starttime + 100000 - now
    timeleft /= 10
    timeleftimage = font.render(str(timeleft/100), 1, (255,0,0))
    timeleftimagerect = timeleftimage.get_rect()
    timeleftimagerect.left += WIDTH - timeleftimagerect.width 
    surface.blit(timeleftimage, timeleftimagerect)
    if timeleft < 0: break
    
    pygame.display.flip()
    pygame.time.delay(1000)


while 1:
    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.time.delay(100)
