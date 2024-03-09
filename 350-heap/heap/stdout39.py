from latextool_basic import *
p = Plot()
edges={20: [10, 7],
10: [ 9, 1],
7: [ 0, 5],
9: [ 2],
}
drawheap(p, edges, include_array=False)
print(p)
