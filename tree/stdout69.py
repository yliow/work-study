from latextool_basic import *
p = Plot()

Graph.r = 0.3
Graph.background = 'white'

edges = {'10':['2','18'],
         '4':['2'],
         '2':['0','4'],
         '4':['3'],
         '18':['17','20'],
        }
  
pos = bintreepositions(edges=edges,
                       node_hsep=0.7)
                       
for k,v in pos.items():
    x,y = v
    p += Graph.node(x=x, y=y, name='%s' % k, label=r'\texttt{%s}' % k)
      
for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        p += Graph.arc(names=[k,x])

print(p)
