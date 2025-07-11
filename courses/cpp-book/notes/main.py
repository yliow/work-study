from latextool_basic import *
from latexcircuit import *
p = Plot()

#p += Grid(x0=-5, y0=-5, x1=5, y1=5)

p += Rect(1, 2, 9, 5, s=r"If \texttt{f()} is not virtual, the decision of which \texttt{f()} to use is based on the pointer's type P.\\ \textbf{Static/early binding.}", linewidth=0.1, linecolor='red', innersep=0.3)

p += Rect(1, -2, 9, 1, s=r"If \texttt{f()} not virtual, the decision of which \texttt{f()} to use is based on the object's class C.\\ \textbf{Dynamic/late binding.}", linewidth=0.1, linecolor='red', innersep=0.3)
p += Rect(-3.5,2.5,-2.5,4.5,linewidth=0.05)
p += Line(points=[(-2.5,3.5),(1,3.5)], linestyle='dashed',linecolor='red',linewidth=0.1)
p += Line(points=[(-2.5,-0.5),(1,-0.5)], linestyle='dashed',linecolor='red',linewidth=0.1)
p += Line(points=[(-3,3.5),(-3,0.5)], endstyle='>',linewidth=0.05)
p += ellipse(center=(-3,-0.5), height=2,width=3,linewidth=0.05)
X = POINT(x=-3.9, y=3.5, r=0, label='pointer to object')
Y = POINT(x=-4.9, y=-0.5, r=0, label='object')
p += str(X)
p += str(Y)
print(p)

