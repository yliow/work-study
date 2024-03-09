from latextool_basic import *
from drawheap import *  
p = Plot()
edges={'10':['5','8'],
       '5':['9', '1'],
       '8':['3', '7'],
       '9':['0', '2'],
       }
drawheap(p, edges)
print(p)

