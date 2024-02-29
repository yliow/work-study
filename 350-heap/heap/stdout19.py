from latextool_basic import *
from drawheap import *
p = Plot()
edges={'10':['5','8'],
       '5':['3','2'],
       '8':['4','6'],
       '3':['1','0']
       }
drawheap(p, edges, include_array=False)
print(p)
