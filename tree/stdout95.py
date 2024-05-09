from latextool_basic import *
p = Plot()

Graph.r = 0.3
Graph.background = 'white'

edges = {'10':['','5'],
        }
  
pos = bintreepositions(edges=edges,
                       node_hsep=0.7)
                       
for k,v in pos.items():
    x,y = v
    p += Graph.node(x=x, y=y, name='%s' % k, label=r'\texttt{%s}' % k)
    if k == '10':
        p += Graph.node(x=x+1.4,y=y, label=r'$b \rightarrow b + 1$', linewidth=0)
    else:
        p += Graph.node(x=x+0.6,y=y, label='0', linewidth=0)
    
for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        #if (k,x) in [('10','2'), ('2','5'), ('5','3')]:
        #    p += Graph.arc(names=[k,x], linewidth=0.1, linecolor='red')
        #else:
        if 1:
            p += Graph.arc(names=[k,x])


print(p)
