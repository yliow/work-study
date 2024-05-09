from latextool_basic import *
from drawheap import *
p = Plot()
edges={'10':['0','8'],
       '0':['5','2'],
       '8':['4','6'],
       '5':['1','3']
       }
drawheap(p, edges, include_array=False)
print(p)
