from latextool_basic import *
from drawheap import *
p = Plot()
edges={'10':['5','7'],
       '5':['2', '1'],
       '7':['','0'],
       }
drawheap(p, edges, include_array=False)
print(p)
