from latextool_basic import *
p = Plot()
edges={10: [ 5, 8],
5: [ 9, 1],
8: [ 0, 7],
9: [ 2],
}
drawheap(p, edges, include_array=False)
print(p)
