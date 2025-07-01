from latextool_basic import *
from latexcircuit import *
p = Plot()
p += Grid(x0=-4,y0=-4,x1=5,y1=5)
p += Rect(-2,0.5,3,2.5, label=r'\large{\texttt{for  (\ \ \ \ ;\ \ \ \ ;\ \ \ \ ;)}}', linewidth=0)
p += Rect(-3,-2,5,3, linewidth=0.2)
p += Rect(-1,-1,3,1, linewidth=0.1)
p += Rect(-0.5,-0.5,2.5,0.5, linewidth=0.05, label=r'\texttt{\textbf{continue;}}')


p += Line(points=[(2.5,0),(4, 0)], linewidth=0.1, linecolor='red')
p += Line(points=[(4,0),(4,2.5)], linewidth=0.1, linecolor='red')
p += Line(points=[(4,2.5),(2.5,2.5)], linewidth=0.1, linecolor='red')
p += Line(points=[(2.5,2.5),(2.5,1.5)], linewidth=0.1, linecolor='red', endstyle='>')

print(p)

