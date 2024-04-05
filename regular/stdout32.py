from latextool_basic import *
print(automata(layout="""
   B  C
A
   D  E  F  G
""",
edges="A,$\ep$,B|B,$a$,C|C,$\ep$,B|D,$b$,E|E,$b$,F|F,$a$,G|A,$\ep$,D",
A='initial|label=$q_0$',
B='accept|label=$q_1$',
C='accept|label=$q_2$',
D='label=$q_3$',
E='label=$q_4$',
F='label=$q_5$',
G='accept|label=$q_6$',
))
