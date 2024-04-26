from latextool_basic import *
print(automata(layout=r"""
   B C
A       D
""",
A = "label=$1$",
B = "label=$2$",
C = "label=$3$",
D = "label=$4$",
edges=r"A,$\ep,\ep\rightarrow\$$,B|C,$\ep,\$\rightarrow \ep$,D",
))
