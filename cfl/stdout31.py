s = r'''
from latextool_basic import *
p = Plot()
m = [['$\{A_a,B_a,D_a\}$','$\{A_a,B_a,D_a\}$'],
     ['$\{S_{(1,1)(1,2)},$ $A_{(1,1)(1,2)}$, $C_{(1,1)(1,2)}$, $S_{(1,1)(1,2)}$, $D_{(1,1)(1,2)} \}$',''],
     ]
cyk(p, m, w='aa',width=6, height=1.4, fontsize='footnotesize')
print(p)
'''
from latextool_basic import *
execute(s, print_source=False)
