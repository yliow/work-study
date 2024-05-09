from latextool_basic import *
p = Plot()
edges={'a':['b','d'],
  'b':['e','f'],
  'd':['h','o'],
  'e':['k','l'],
  'h':['','m'],
  'o':['p','j'],
  #'p':['q','r'],
  }
pos = bintreepositions(edges=edges)
Graph.r = 0.3
for k,(x,y) in pos.items():
    p += Graph.node(x=x, y=y, name=k, label=r'$%s$' % k)
for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        p += Graph.arc(names=[k,x])

x,y = pos['p']
p += Graph.node(x=x-0.4, y=y-1, name='q', label='$q$')        
p += Graph.node(x=x+0.4, y=y-1, name='r', label='$r$')        
p += Graph.arc(names=['p','q'])        
p += Graph.arc(names=['p','r'])        

print(p)
