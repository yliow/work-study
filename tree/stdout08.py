from latextool_basic import *
p = Plot()
edges={'a':['b','c'],
  'b':['d','e'],
  'c':['f','g'],
  'd':['h', 'i'],
  'e':['','k'],
  'f':['l','m']
  }
pos = bintreepositions(edges=edges)
Graph.r = 0.3
for k,(x,y) in pos.items():
    p += Graph.node(x=x, y=y, name=k, label=r'$%s$' % k)
for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        p += Graph.edge(names=[k,x])
print(p)
