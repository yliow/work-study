from latextool_basic import *
p = Plot()
xs = [9, 8, 4, 7, 3, 2, 1, 0, 6]
edges = array_to_edges(xs)
drawheap(p, edges, include_array=False)
print(p)
