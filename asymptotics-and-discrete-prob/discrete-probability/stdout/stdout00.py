import random; random.seed()

HEAD = "HEAD"
TAIL = "TAIL"
S = [HEAD, TAIL] # outcomes

def toss_coin():
    r = random.randrange(2)
    if r == 0: 
        return TAIL
    else:
        return HEAD

n = 20 # number of experiments to perform
for i in range(n):
    print("experiment", i, "... outcome:", toss_coin())
