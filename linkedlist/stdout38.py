from latextool_basic import *

print(automata(layout="""
A  B  F
C  D  E
""",
A="label=$0$",
B="label=$1$",
C="label=$3$",
D="label=$4$",
E="label=$5$",
F="label=$2$",
edges='A,,A|A,,B|B,,D|D,,E|B,,E|C,,D|C,,B'
))
