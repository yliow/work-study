from latextool_basic import *
p = Plot()
xs = [0, 1, 2, 3, 4, 6, 7, 8, 9]
edges = array_to_edges(xs)
pos = drawheap(p, edges, include_array=False)

x,y = pos[9]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='9')
x,y = pos[8]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='8')
x,y = pos[7]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='7')
x,y = pos[6]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='6')
x,y = pos[4]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='4')
x,y = pos[3]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='3')
x,y = pos[2]; p += Graph.node(x=x, y=y, r=BinTree.node_width, background='red!10', label='2')

p += Graph.edge(names=[0,2], linecolor='white', linewidth=0.1); p += Graph.edge(names=[0,2], linestyle='dashed')
p += Graph.edge(names=[3,9], linecolor='white', linewidth=0.1); p += Graph.edge(names=[3,9], linestyle='dashed')
p += Graph.edge(names=[3,8], linecolor='white', linewidth=0.1); p += Graph.edge(names=[3,8], linestyle='dashed')
p += Graph.edge(names=[2,7], linecolor='white', linewidth=0.1); p += Graph.edge(names=[2,7], linestyle='dashed')
p += Graph.edge(names=[2,6], linecolor='white', linewidth=0.1); p += Graph.edge(names=[2,6], linestyle='dashed')
p += Graph.edge(names=[1,4], linecolor='white', linewidth=0.1); p += Graph.edge(names=[1,4], linestyle='dashed')
p += Graph.edge(names=[1,3], linecolor='white', linewidth=0.1); p += Graph.edge(names=[1,3], linestyle='dashed')

print(p)
