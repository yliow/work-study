from latextool_basic import *
p = Plot()
r, crosses, nodes, lines = adjlist(xs=[[0],[4,5],[], [1,4], [5],[]])
p += r
_ = r[1]
_.linecolor = 'blue'
_.background = 'blue!10'
p += _
for k,v in crosses.items():
    for _ in v: p += _
    
for k,v in nodes.items():
    for _ in v: p += _
# redraw nodes[1]
for _ in nodes[1]:
    _[0].background = 'blue!10'
    _[0].linecolor = 'blue'
    p += _

for k,v in lines.items():
    for _ in v: p += _
# redraw lines[1]:
for _ in lines[1]:
    _.linecolor = 'blue'
    p += _

print(p)
