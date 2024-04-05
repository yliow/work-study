from latextool_basic import *
print(automata(layout="""
   D  E  F  G
""",
edges="D,$a$,D|D,$b$,E|E,$b$,F|F,$a$,G|G,$\ep$,D",
D='initial|accept|label=$q_3$',
E='label=$q_4$',
F='label=$q_5$',
G='accept|label=$q_6$',
))
