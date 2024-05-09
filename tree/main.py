from latextool_basic import *
d = 0
p = Plot()
p += Graph.node(x=d + 0, y=0, name='a')
p += Graph.node(x=d + -1, y=-1, name='b')
p += Graph.node(x=d + -2, y=-2, name='c')
p += Graph.edge(names=['a', 'b'])
p += Graph.edge(names=['b', 'c'])

d = 3
p += Graph.node(x=d + 0, y=0, name='a1')
p += Graph.node(x=d + -1, y=-1, name='b1')
p += Graph.node(x=d + 0, y=-2, name='c1')
p += Graph.edge(names=['a1', 'b1'])
p += Graph.edge(names=['b1', 'c1'])

d = 6
p += Graph.node(x=d + 0, y=0, name='a2')
p += Graph.node(x=d + +1, y=-1, name='b2')
p += Graph.node(x=d + 0, y=-2, name='c2')
p += Graph.edge(names=['a2', 'b2'])
p += Graph.edge(names=['b2', 'c2'])

d = 9
p += Graph.node(x=d + 0, y=0, name='a3')
p += Graph.node(x=d + 1, y=-1, name='b3')
p += Graph.node(x=d + 2, y=-2, name='c3')
p += Graph.edge(names=['a3', 'b3'])
p += Graph.edge(names=['b3', 'c3'])

d = 0
p += Graph.node(x=d + 0, y=-4, name='a4')
p += Graph.node(x=d + -1, y=-4 - 1, name='b4')
p += Graph.node(x=d + +1, y=-4 - 1, name='c4')
p += Graph.edge(names=['a4', 'b4'])
p += Graph.edge(names=['a4', 'c4'])

print(p)

