from latextool_basic import *

p = Plot()
m = [['','','','','',''],
     ['','','','','',''],
     ['?','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ]
c = cyk(p, m, w='baaaab',
        background={(0,0):'blue!10', (1,1):'blue!10', (1,0):'red!10', (0,2):'red!10'},
        fontsize='small')
p += Line(points=[c[0][0].center(), c[1][0].center()], endstyle='>', linewidth=0.1)     
p += Line(points=[c[1][1].center(), c[0][2].center()], endstyle='>', linewidth=0.1)     
print(p)
