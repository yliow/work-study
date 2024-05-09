from latextool_basic import *
p = Plot()
edges={'a':['b','o'],
  'b':['e','f'],
  'o':['','d'],
  'd':['h','j'],
  'e':['k','l'],
  #'h':['','m'],
  }
pos = bintreepositions(edges=edges)
Graph.r = 0.3
for k,(x,y) in pos.items():
    p += Graph.node(x=x, y=y, name=k, label=r'$%s$' % k)
for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        p += Graph.arc(names=[k,x])

x,y = pos['h']
p += Graph.node(x=x+0.3, y=y-1.1, name='m', label=r'$%s$' % 'm')
p += Graph.arc(names=['h', 'm'])
        
print(p)
