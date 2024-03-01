from latextool_basic import *
from drawheap import *
p = Plot()
edges={'28':['23','25'],
       '23':['10','8'],
       '25':['24','14'],
       '10':['9'],
       }
drawheap(p, edges, include_array=False)
print(p)
