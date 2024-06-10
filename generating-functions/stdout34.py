from latextool_basic import *
from latexcircuit import *
from labeledpoint import *
L = POLY_LINEWIDTH
p = Plot()
V = regularpoly(6)
for i in [0]:
    V1 = V[:]
V1 = [(x+i*3.25, y) for (x,y) in V1]
p += polygon(points=V1, 
fill=False,
drawboundary=True,
closed=True,
)
p += polygon(points=[V1[4],V1[5],V1[i]], 
fill=False, linewidth=0.01,
drawboundary=True,
closed=True,
)
p += polygon(points=[V1[0],V1[1],V1[3]], 
fill=False, linewidth=0.01,
drawboundary=True,
closed=True,
)
print(p)
