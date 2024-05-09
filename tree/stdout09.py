from latextool_basic import *
p = Plot()
edges={'+':['*','c'],
  '*':['-',r'e'],
  'c':['f','1'],
  '-':['3', '5'],
  r'e':['z','2'],
  'f':['0','7'],
  }
pos = bintreepositions(edges=edges)
Graph.r = 0.3
for k,(x,y) in pos.items():
    if k == 'c':
        p += Graph.node(x=x, y=y, name=k, label=r'\texttt{+}')
    elif k == 'e':
        p += Graph.node(x=x, y=y, name=k, label=r'\texttt{\%}')
    elif k == 'f':
        p += Graph.node(x=x, y=y, name=k, label=r'\texttt{*}')
    elif k == 'z':
        p += Graph.node(x=x, y=y, name=k, label=r'\texttt{7}')
    else:
        p += Graph.node(x=x, y=y, name=k, label=r'\texttt{%s}' % k)    
for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        p += Graph.edge(names=[k,x])
print(p)
