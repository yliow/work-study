from latextool_basic import *
p = Plot()

Graph.r = 0.3
Graph.background = 'white'

edges = {'14':['9','18'],
         '9':['5','13'],
         '18':['15','22'],
         '5':['0','8'],
         '13':['10'],
         '22':['21','31'],
         '8':['7'],
         '10':['','11'],
         '21':['19']
  }
pos = bintreepositions(edges=edges,
                       node_width=0.6)
for k,v in pos.items():
    x,y = v
    p += Graph.node(x=x, y=y, name=k, label=r'\texttt{%s}' % k)
      
for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        p += Graph.arc(names=[k,x])

print(p)
