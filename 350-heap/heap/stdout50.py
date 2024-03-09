from latextool_basic import *
from drawheap import *  
p = Plot()
edges={'12': ['10','8'],
       '10': ['9', '3'],
       '8': ['0', '7'],
       '9': ['2', '5'],
     }
drawheap(p, edges, include_array=False)
print(p)
