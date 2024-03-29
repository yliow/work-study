from latextool_basic import *
p = Plot()
dfa(p,
state=r'$q_1$',
body_w=1.5, body_h=1,
tape=['b','a','a','a', 'b', r'\SPACE',r'\SPACE',r'\SPACE'],
head_index=1,
vsep=0.7,
w=0.5, h=0.5
)
print(p)
