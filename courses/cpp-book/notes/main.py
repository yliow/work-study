from latextool_basic import *
from latexcircuit import *
D = r'''



int sum = 0;

    for ( int i = 3;     i < 5;     i = i + 1 )


        sum = sum + i;



'''.strip()

p = Plot()
code(p, D, x=-4.5, y=0, border_linewidth=0.05, innersep=0.6)

#p += Grid(x0=-5,y0=-10,x1=10,y1=2)

p += ellipse(x0=-5,y0=-8,x1=1,y1=-4, linewidth=0.1)

p += Rect(x0=3,y0=-8,x1=10,y1=-4, linewidth=0.1)
p += Rect(x0=-4,y0=-2.9,x1=2,y1=-2.71, linewidth=0.12, linecolor='red')
#p += Rect(x0=7.5,y0=-2,x1=11,y1=1, linewidth=0.2, linecolor='red', align='l', font='\normalsize\bfseries', s = 'When you leave the for-loop, \\ variable i is destroyed')

p += Rect(x0=5,y0=-5.5,x1=8,y1=-4.5, linewidth=0.1, label='7')

X = POINT(x=-2.3, y=-3.9, r=0, label='CPU', anchor='flushtopleft')
Y = POINT(x=6.1, y=-3.9, r=0, label='main', anchor='flushtopleft')
Z = POINT(x=5, y=-5, r=0, label='sum', anchor='east')

p += str(X)
p += str(Y)
p += str(Z)

print(p)

