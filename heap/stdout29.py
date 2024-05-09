from latextool_basic import *
p = Plot()
edges={'10':['9','8'],
       '9':['5', '1'],
       '8':['0', '7'],
       '5':['2'],
     }
#BinTree.node_hsep=0.2
drawheap(p, edges, include_array=False)
print(p)
