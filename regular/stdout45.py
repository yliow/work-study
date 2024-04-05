from latextool_basic import *
print(automata(layout="""
A  B  E  F  

C  D  G  H
""",
edges="A,$a$,B|A,$b$,C|B,$a$,E|B,$b$,D|C,$b$,A|C,$a$,D|D,$b$,B|E,$a$,F|G,$a$,H|D,$a$,G|F,$a$,A|H,$a$,C|E,$b$,G|G,$b$,E|F,$b$,H|H,$b$,F",
A='initial|accept|label=$q_0$',
B='label=$q_1$',
C='accept|label=$q_4$',
D='label=$q_5$',
E='accept|label=$q_2$',
G='accept|label=$q_6$',
H='label=$q_7$',
F='label=$q_3$',
xscale=1.3,
))
