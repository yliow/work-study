from latextool_basic import *
d = positions(r'''
A
B
C
''')
p = Plot()

Graph.r = 0.3
x,y = d['A']; p += Graph.node(x=x, y=y, label='$q_0$', name='A')
x,y = d['B']; p += Graph.node(x=x, y=y, label='$q_3$', name='B')
x,y = d['C']; p += Graph.node(x=x, y=y, label='$q_1$', name='C')

p += Graph.arc(names=['A','B'], label=r'$\epsilon$', anchor='left')
p += Graph.arc(names=['B','C'], label=r'$\epsilon$', anchor='left')

print(p)
