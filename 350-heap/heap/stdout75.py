from latextool_basic import *
p = Plot()
xs = [4, 3, 2, 0, 1, 6, 7, 8, 9]
edges = array_to_edges(xs)
pos = drawheap(p, edges, include_array=False)

x,y = pos[9]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='9')
x,y = pos[8]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='8')
x,y = pos[7]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='7')
x,y = pos[6]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='6')

p += Graph.edge(names=[0,9], linecolor='white', linewidth=0.1); p += Graph.edge(names=[0,9], linestyle='dashed')
p += Graph.edge(names=[0,8], linecolor='white', linewidth=0.1); p += Graph.edge(names=[0,8], linestyle='dashed')
p += Graph.edge(names=[2,7], linecolor='white', linewidth=0.1); p += Graph.edge(names=[2,7], linestyle='dashed')
p += Graph.edge(names=[2,6], linecolor='white', linewidth=0.1); p += Graph.edge(names=[2,6], linestyle='dashed')

print(p)
