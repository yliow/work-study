from latextool_basic import *
from drawheap import *
p = Plot()
edges={'10':['5','8'],
       '5':['0','2'],
       '8':['4','6'],
       '0':['1','3']
       }
drawheap(p, edges, include_array=False)
