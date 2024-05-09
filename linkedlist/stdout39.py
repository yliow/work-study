from latextool_basic import *
p = Plot()
r, crosses, nodes, lines = adjlist(xs=[[0],[4,5],[], [1,4], [5],[]])
p += r
for k,v in crosses.items():
    for _ in v: p += _
for k,v in nodes.items():
    for _ in v: p += _
for k,v in lines.items():
    for _ in v: p += _

print(p)
