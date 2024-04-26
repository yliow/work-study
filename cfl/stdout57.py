from latextool_basic import *
print(automata(layout="""
A  B
D  C
""",
edges=r"A,$(\ep,\ep\rightarrow\$)$,B|B,$(a, \ep\rightarrow a)$,B|B,$(b,a\rightarrow\ep)$,C|C,$(\ep,\ep\rightarrow \$)$,D",
A="initial|label=$1$",
B="label=$2$",
C="label=$3$",
D="label=$4$",
))
