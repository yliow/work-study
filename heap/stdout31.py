from latextool_basic import *
p = Plot()
edges={'20':['10','8'],
       '10':['9', '1'],
       '8':['0', '7'],
       '9':['2', '5'],
     }
#BinTree.node_hsep=0.2
drawheap(p, edges, include_array=False)
print(p)
