from latextool_basic import *

m = [['','','','','',''],
     ['','','','','',''],
     ['','?','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ]
p = Plot()
c = cyk(p, m, w='baaaab', background={(0,1):'blue!10', (1,1):'red!10', (1,2):'blue!10', (0,3):'red!10'},fontsize='small')
p += Line(points=[c[0][1].center(), c[1][1].center()], endstyle='>', linewidth=0.1)
p += Line(points=[c[1][2].center(), c[0][3].center()], endstyle='>', linewidth=0.1)
print(p)
