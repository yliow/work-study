from latextool_basic import *
from drawheap import *
p = Plot()
edges={'5':['8','10'],
       '8':['12'],
       '10':['13','15'],
       }
drawheap(p, edges, include_array=False)
print(p)
