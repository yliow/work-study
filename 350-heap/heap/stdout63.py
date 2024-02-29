from latextool_basic import *
p = Plot()
xs = [6, 8, 4, 7, 3, 2, 1, 0, 9]
edges = array_to_edges(xs)
pos = drawheap(p, edges, include_array=False)
