import random; random.seed()

HEAD = "HEAD"
TAIL = "TAIL"
S = [HEAD, TAIL] # outcomes

def toss_coin():
    if random.randrange(2) == 0: 
        return TAIL
    else:
        return HEAD

n = 20 # number of experiments to perform
outcomes = []
for i in range(N):
    outcome = toss_coin()
    print("experiment", i, "... outcome:", outcome)
    outcomes.append(outcome)

table = {}
table[HEAD] = outcomes.count(HEAD)
table[TAIL] = outcomes.count(TAIL)

print("number of experiments:", n)
print("number of heads:", table[HEAD])
print("number of tails:", table[TAIL])
print("probability of getting head:", table[HEAD] / float(n))
print("probability of getting tail:", table[TAIL] / float(n))
