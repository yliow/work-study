from latextool_basic import *
from drawheap import *  
p = Plot()
edges={'10':['9','8'],
       '9':['5', '1'],
       '8':['3', '7'],
       '5':['0', '2'],
       }
drawheap(p, edges)
print(p)
