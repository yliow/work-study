from latextool_basic import *
p = Plot()
xs = [6, 8, 4, 7, 3, 2, 1, 0, 9]
edges = array_to_edges(xs)
pos = drawheap(p, edges, include_array=False)

x,y = pos[9]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='9')
p += Graph.edge(names=[7,9], linecolor='white', linewidth=0.1)
p += Graph.edge(names=[7,9], linestyle='dashed')

print(p)
