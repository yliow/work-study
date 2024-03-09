from latextool_basic import *
p = Plot()
edges={5: [10, 8],
10: [ 9, 1],
8: [ 0, 7],
9: [ 2],
}
drawheap(p, edges, include_array=False)
print(p)
