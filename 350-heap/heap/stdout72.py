from latextool_basic import *
p = Plot()
xs = [6, 3, 4, 0, 1, 2, 7, 8, 9]
edges = array_to_edges(xs)
pos = drawheap(p, edges, include_array=False)

x,y = pos[9]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='9')
x,y = pos[8]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='8')
x,y = pos[7]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='7')

p += Graph.edge(names=[0,9], linecolor='white', linewidth=0.1); p += Graph.edge(names=[0,9], linestyle='dashed')
p += Graph.edge(names=[0,8], linecolor='white', linewidth=0.1); p += Graph.edge(names=[0,8], linestyle='dashed')
p += Graph.edge(names=[4,7], linecolor='white', linewidth=0.1); p += Graph.edge(names=[4,7], linestyle='dashed')

print(p)
