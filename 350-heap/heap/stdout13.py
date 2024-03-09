from latextool_basic import *
from drawheap import *  
p = Plot()
edges={'10':['5','8'],
       '5':['2', '1'],
       '8':['3', '7'],
       '2':['0', '9'],
       }
drawheap(p, edges)
print(p)
