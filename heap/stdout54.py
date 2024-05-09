from latextool_basic import *
p = Plot()
edges={'12': ['9','8'],
       '9': ['1', '3'],
       '8': ['0', '7'],
       '1': ['2', '5'],
     }
drawheap(p, edges, include_array=False)
p += Line(names=['1', '5'], endstyle='>', startstyle='>', linewidth=0.03, linecolor='red', bend_left=90)     
print(p)
