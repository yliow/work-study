s = r'''
from latextool_basic import *
p = Plot()
m = [['$\{B,C\}$','$\{A\}$','$\{A\}$','$\{A\}$','$\{A\}$','$\{B,C\}$'],
     ['$\emptyset$','$\{C\}$','$\{C\}$','$\{C\}$','$\{S\}$',''],
     ['$\{A\}$','$\{S\}$','$\{S\}$','$\{B\}$','',''],
     ['$\{C\}$','$\emptyset$','$\{S\}$','','',''],
     ['$\{S\}$','$\{B\}$','','','',''],
     ['$\{B,S\}$','','','','',''],
     ]
cyk(p, m, w='baaaab',fontsize='small')
print(p)
'''
from latextool_basic import *
execute(s, print_source=False)
