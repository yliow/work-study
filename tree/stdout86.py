from latextool_basic import *
p = Plot()

Graph.r = 0.3
Graph.background = 'white'

edges = {'10':['2','18'],
         '2':['0','5'],
        }
  
pos = bintreepositions(edges=edges,
                       node_hsep=0.7)
                       
for k,v in pos.items():
    x,y = v
    if k == '2':
        p += Graph.node(x=x, y=y, name='%s' % k, label=r'\texttt{%s}' % k,
                                linecolor='red', linewidth=0.1,r=0.35)
    else:
        p += Graph.node(x=x, y=y, name='%s' % k, label=r'\texttt{%s}' % k)
      
for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        #if (k,x) in [('10','2'), ('2','0')]:
        #    p += Graph.arc(names=[k,x], linewidth=0.1, linecolor='red')
        #else:
        if 1:
            p += Graph.arc(names=[k,x])


print(p)
