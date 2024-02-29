from latextool_basic import *
p = Plot()
xs = [1, 0, 9, 8, 3, 2, 4, 7, 6]
edges = array_to_edges(xs)
drawheap(p, edges, include_array=False)

print(p)
