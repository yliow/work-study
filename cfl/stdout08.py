s = r'''
from latextool_basic import *

m = [['$\{B_b,C_b\}$','$\{A_a\}$','$\{A_a\}$','$\{A_a\}$','$\{A_a\}$','$\{B_b,C_b\}$'],
     ['$\emptyset$','$\{C_{(1,2),(1,3)}\}$','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ]
p = Plot()
cyk(p, m, w='baaaab', background={(0,1):'blue!10', (0,2):'blue!10'},fontsize='small')
print(p)
'''
from latextool_basic import *
execute(s)
