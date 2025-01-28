from latextool_basic import *
from pyutil import *

s = r'''
# file: main08a.py
import random; random.seed()
n = 1000000
count = 0
for _ in range(n):
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    if a == 6 and b == 6:
        count += 1
print(count / n, 1 / 36)
'''.strip()
print(r'''\begin{console}[frame=single,fontsize=\footnotesize]
%s
\end{console}''' % s) 
writefile('main08a.py', s)
print(r'''The output is
%s''' % shell('python main08a.py', fontsize=r'\footnotesize'))
