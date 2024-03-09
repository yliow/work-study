from latextool_basic import *
p = Plot()
edges={'10':['5','7'],
       '5':['2', '1'],
       '7':['0', '8'],
     }
#BinTree.node_hsep=0.2
drawheap(p, edges, include_array=False)
print(p)
