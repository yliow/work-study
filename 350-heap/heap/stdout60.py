from latextool_basic import *
p = Plot()
xs = [1, 8, 9, 7, 3, 2, 4, 0, 6]
edges = array_to_edges(xs)
drawheap(p, edges,
    include_array=False)

p += r'\node [ellipse, draw=red, fit=(9) (2) (4), line width=0.1cm, inner sep=0.0cm] {};'
p += r'\node [ellipse, draw=red, fit=(3) (0) (8) (7) (6), line width=0.1cm, inner sep=0.0cm] {};'

print(p)
