from latextool_basic import *
p = Plot()

d = positions('''
   f
   g
  h j
  i
''', xscale=0.7)
edges={'f':['g'],
       'g':['h','j'],
       'h':['i'],
}

Graph.r = 0.3

for k in 'fghij':
    x,y = d[k]
    p += Graph.node(x=x, y=y, label=r'\texttt{%s}' % k, name=k)

for k in edges:
    for v in edges[k]:
        p += Graph.edge(names=[k,v])
        
print(p)
