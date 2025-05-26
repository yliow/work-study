import random; random.seed()

def roll_dice():
    return random.randrange(6) + 1

def gain():
    r0 = roll_dice()
    if r0 == 6:
        return 40 - 10 # 10 to play the game
    else:
        r1 = roll_dice()
        if r0 == r1:
            return 20 - 10
        else:
            return 0 - 10

total = 0
N = 1000000
for i in range(N):
    total += gain()
print("average gain:", total / float(N)) 
