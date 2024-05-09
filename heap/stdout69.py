from latextool_basic import *
p = Plot()
xs = [7, 6, 4, 0, 3, 2, 1, 8, 9]
edges = array_to_edges(xs)
pos = drawheap(p, edges, include_array=False)

x,y = pos[9]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='9')
x,y = pos[8]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='8')
p += Graph.edge(names=[0,9], linecolor='white', linewidth=0.1); p += Graph.edge(names=[0,9], linestyle='dashed')
p += Graph.edge(names=[0,8], linecolor='white', linewidth=0.1); p += Graph.edge(names=[0,8], linestyle='dashed')

print(p)
