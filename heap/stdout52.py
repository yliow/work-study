from latextool_basic import *
p = Plot()
edges={'12': ['1','8'],
       '1': ['9', '3'],
       '8': ['0', '7'],
       '9': ['2', '5'],
     }
drawheap(p, edges, include_array=False)
p += Line(names=['1', '9'], startstyle='>', endstyle='>', linecolor='red', linewidth=0.03, bend_right=60)     
print(p)
