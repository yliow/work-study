from latextool_basic import *

p = Plot()
m = [['$\{B_b,C_b\}$','$\{A_a\}$','$\{A_a\}$','$\{A_a\}$','$\{A_a\}$','$\{B_b,C_b\}$'],
     ['$\emptyset$','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ]
cyk(p, m, w='baaaab', background={(0,0):'blue!10', (0,1):'blue!10'},fontsize='small')
print(p)
