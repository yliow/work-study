from latextool_basic import *
p = Plot()
edges={20: [10, 5],
10: [ 9, 1],
5: [ 0, 7],
9: [ 2],
}
drawheap(p, edges, include_array=False)
print(p)
