from latextool_basic import *
p = Plot()
p += Circle(x=0,y=0,r=2,background='blue!10')
deg = 90
for i in range(10):
    if i not in [0,2,4,6,8,1,5]:
        p += r'\draw (%s: 2.3) node {$%s$};' % (deg, i)
    else:
        p += r'\draw (%s: 2.3) node {\textwhite{$%s$}};' % (deg, i)
    deg -= 360/10
print(p)

