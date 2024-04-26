from latextool_basic import *
p = Plot()
m = [['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['?','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ]
c = cyk(p, m, w='baaaab', fontsize='small',
    background={(0,0):'blue!10',  (2,1):'blue!10',
                (1,0):'red!10',   (1,2):'red!10',
                (2,0):'green!10', (0,3):'green!10',
    })
p += Line(points=[c[0][0].center(), c[2][0].center()], endstyle='>', linewidth=0.1)
p += Line(points=[c[2][1].center(), c[0][3].center()], endstyle='>', linewidth=0.1)
print(p)
