from latextool_basic import *
from drawheap import *
p = Plot()
edges={'10':['0','8'],
       '0':['5','2'],
       '8':['4','6'],
       '5':['1','3']
       }
drawheap(p, edges, include_array=False)
p += Line(names=['0', '5'], linewidth=0.03, linecolor='red',
          bend_right=60, endstyle='>', startstyle='>')       
print(p)
