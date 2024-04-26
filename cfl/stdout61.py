from latextool_basic import *
print(automata(layout=r"""
   B C
A       D
""",
A = "label=$1$",
B = "label=$2$",
C = "label=$2$",
D = "label=$3$",
edges=r"A,$\ep,\ep\rightarrow\$$,B|C,$b,a\rightarrow \ep$,D",
))
