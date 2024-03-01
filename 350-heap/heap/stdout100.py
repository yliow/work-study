from latextool_basic import *
from drawheap import *
p = Plot()
edges={16: [13, 7],
       13: [3, 11],
       7: [5, 4],
       }
drawheap(p, edges, include_array=False)
print(p)
