from latextool_basic import *
p = Plot()

Graph.r = 0.3
Graph.background = 'white'

edges = {'10':['7', '18'],
         '5':['0', '6'],
         '7':['5', '8'],
        }
  
pos = bintreepositions(edges=edges,
                       node_hsep=0.7)
                       
for k,v in pos.items():
    x,y = v
    p += Graph.node(x=x, y=y, name='%s' % k, label=r'\texttt{%s}' % k)
      
for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        if (k,x) in [('10','2'), ('2','5'), ('5','3')]:
            p += Graph.arc(names=[k,x], linewidth=0.1, linecolor='red')
        else:
            p += Graph.arc(names=[k,x])


print(p)
