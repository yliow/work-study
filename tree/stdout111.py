from latextool_basic import *
p = Plot()

Graph.r = 0.3
Graph.background = 'white'

edges = {'6':['4', '9'],
         '4':['3', '5'],
         '15':['12','22'],
         '10':['6','15'],
         '22':['18','28'],
         '18':['17','19'],
        }
  
pos = bintreepositions(edges=edges,
                       node_hsep=0.1, node_width=0.6)
                       
for k,v in pos.items():
    x,y = v
    if k == 'x':
        p += Graph.node(x=x, y=y, name='%s' % k, label=r'\texttt{%s}' % k)
    else:
        p += Graph.node(x=x, y=y, name='%s' % k, label=r'\texttt{%s}' % k)
      
for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        #if (k,x) in [('10','2'), ('2','5'), ('5','3')]:
        #    p += Graph.arc(names=[k,x], linewidth=0.1, linecolor='red')
        #else:
        if 1:
            p += Graph.arc(names=[k,x])

print(p)
