from latextool_basic import *
from drawheap import *
p = Plot()
edges={'5':['2','0'],
       '2':['6','1'],
       '0':['','3'],
       '1':['9']}
drawheap(p, edges, include_array=False)
print(p)
