from latextool_basic import *

m = [['$\{B_b,C_b\}$','$\{A_a\}$','$\{A_a\}$','$\{A_a\}$','$\{A_a\}$','$\{B_b,C_b\}$'],
     ['?','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ['','','','','',''],
     ]
p = Plot()
cyk(p, m, w='baaaab',fontsize='small')
print(p)