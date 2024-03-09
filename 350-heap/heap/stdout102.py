from latextool_basic import *
from drawheap import *
p = Plot()
edges={99: [28, 16],
       28: [23, 25],
       23: [10, 8],
       25: [24, 14],
       10: [9],
       16: [13, 7],
       13: [3],
      }
BinTree.node_hsep=0.01
drawheap(p, edges, node_hsep=0.2, include_array=False)
print(p)
