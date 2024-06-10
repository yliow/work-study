from latextool_basic import *

p = Plot()
As = [3 - x/3.0 for x in range(0, 8)][::-1]
Bs = []
Cs = []
    
hanoi(p, diskss=[As, Bs, Cs])
print(p)
