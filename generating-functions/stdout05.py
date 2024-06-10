from latextool_basic import *

p = Plot()
As = [3 - x/3.0 for x in range(0, 8)][::-1]
Bs = As[:-1]
As = [As[-1]]
Cs = []

def color(w):
    if w<3: return "blue!20"
    else: return "red!20"
hanoi(p, diskss=[Cs, Bs, As], color=color)
print(p)
