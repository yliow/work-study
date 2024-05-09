from latextool_basic import *

print(automata(layout="""
A  B  F
C  D  E
""",
A="label=$a$",
B="label=$b$",
C="label=$c$",
D="label=$d$",
E="label=$e$",
F="label=$f$",
edges='A,,A|A,,B|B,,D|D,,E|B,,E|C,,D|C,,B'
))
