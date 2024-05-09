from latextool_basic import *
from bpt import *

p = Plot()

layout = '''
     A
  X     Y
B C D E F G
'''
d = positions(layout=layout, xscale=1.3, yscale=1.2)
names = layout.replace(' ','').replace('\n','')

M = (f([17,'','','']),
     f([5, 13, '', '']), f([24, 30, '', '']),
     f([2,3],1), f([5,7,8],1), f([14,16],1), f([20, 22],1), f([24,27,29],1), f([33,34,38,39],1),
)

N = get_bpt_nodes(names, M, d)
for v in N.values():
    p += v
    
p += bpt_arc(N['A'], N['X'], 0, r=0)
p += bpt_arc(N['A'], N['Y'], 1, r=0)

p += bpt_arc(N['X'], N['B'], 0, r=0)
p += bpt_arc(N['X'], N['C'], 1, r=0)
p += bpt_arc(N['X'], N['D'], 2, delta=0.2, r=0)

p += bpt_arc(N['Y'], N['E'], 0, r=0)
p += bpt_arc(N['Y'], N['F'], 1, r=0)
p += bpt_arc(N['Y'], N['G'], 2, delta=0.2, r=0)

dllist(p, 'BCDEFG', N)

print(p)
