from latextool_basic import *
d = positions(r'''
A   D
B   E
C   F
''')
p = Plot()

Graph.r = 0.3
for name, label in [('A','$q_0$'),
                    ('B','$q_3$'),
                    ('C','$q_1$'),
                    ('D','$q_0$'),
                    ('E','$q_4$'),
                    ('F','X')]:
    if label != 'X':
        x,y = d[name]; p += Graph.node(x=x, y=y, label=label, name=name)
    else:
        x,y = d[name]
        p += Graph.node(x=x, y=y, label=r'{\large $\times$}', name=name,
                        linewidth=0, background='')
        

p += Graph.arc(names=['A','B'], label=r'$\epsilon$', anchor='left')
p += Graph.arc(names=['B','C'], label=r'$\epsilon$', anchor='left')
p += Graph.arc(names=['A','D'], label=r'$a$', anchor='above')
p += Graph.arc(names=['B','E'], label=r'$a$', anchor='above')
p += Graph.arc(names=['C','F'], label=r'$a$', anchor='above')

print(p)
