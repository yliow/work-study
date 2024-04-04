from latextool_basic import *
print(automata(layout="""
A   B   D

    C
""",
edges="A,$\epsilon$,B|A,$a$,A|A,$a$,C|C,$a,\epsilon$,B|B,$b$,D|D,$a,b$,C",
A="initial|label=$q_0$",
B="label=$q_1$",
C="label=$q_2$",
D="accept|label=$q_3$",
))
