from latextool_basic import *
p = Plot()
edges={'20': [10, 8],
10: [ 9, 1],
8: [ 0, 7],
9: [ 2, '5'],
}
drawheap(p, edges, include_array=False)
p += Line(names=['5', '20'], linecolor='red', endstyle='>', linewidth=0.03)      
print(p)
