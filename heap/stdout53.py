from latextool_basic import *
p = Plot()
edges={'12': ['9','8'],
       '9': ['1', '3'],
       '8': ['0', '7'],
       '1': ['2', '5'],
     }
drawheap(p, edges, include_array=False)
print(p)
