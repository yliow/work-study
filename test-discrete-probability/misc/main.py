from latextool_basic import *
p = Plot()
edges={'7':['3','9'],
 '3':['1','4'],
 '1':['0','2'],
 '4':['5'],
 '5':['','6'],
 '9':['8']}
pos = bintreepositions(edges=edges)

Graph.r = 0.3
for k,(x,y) in pos.items():
    if k in edges.keys():
        p += Graph.node(x=x, y=y, name=k, label=k)
    else:
        p += Graph.node(x=x, y=y, name=k, label=k, background='white')

for k,v in edges.items():
    for x in v:
        if x in [None,'']: continue
        p += Graph.arc(names=[k,x])
print(p)

