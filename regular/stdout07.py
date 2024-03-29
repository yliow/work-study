from latextool_basic import *
print(automata(layout="""
A  B  C
""",
edges="A,$a$,A|A,$b$,B|B,$a$,A|B,$b$,C|C,$a,b$,C",
A="initial|label=$q_0$",
B="label=$q_1$",
C="accept|label=$q_2$",
))
