from latextool_basic import *

m = [['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ]
p = Plot()
m = [['$\{B_b,C_b\}$','$\{A_a\}$','$\{A_a\}$','$\{A_a\}$','$\{A_a\}$','$\{B_b,C_b\}$'],
     ['$\emptyset$','$\{C_{(1,2),(1,3)}\}$','$\{C_{(1,3),(1,4)}\}$','$\{C_{(1,4),(1,5)}\}$','$\{S_{(1,5),(1,6)}\}$',''],
     ['$\{A_{(1,1),(2,2)}\}$','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ]
cyk(p, m, w='baaaab', background={(0,0):'blue!10', (1,1):'blue!10'},fontsize='small')
print(p)