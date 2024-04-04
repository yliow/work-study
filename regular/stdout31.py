from latextool_basic import *
print(automata(layout="""
A         B

C    D
""",
edges="A,$a$,B|A,$b,\epsilon$,C|D,$\epsilon$,B|A,$a$,D|D,$b$,D|D,$a,b$,C",
A="initial|label=$q_0$",
B="label=$q_1$",
C="accept|label=$q_2$",
D="accept|label=$q_3$",
))
