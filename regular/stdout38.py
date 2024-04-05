from latextool_basic import *
print(automata(layout="""
      C  D  E
   A 
      G  H
""",
edges="A,$b$,C|C,$a$,D|D,$b$,E|E,$\ep$,A|A,$a$,G|G,$b$,H|H,$\ep$,A",
A='initial|accept|label=$q_7$',
C='label=$q_9$',
D='label=$q_{10}$',
E='accept|label=$q_{11}$',
G='label=$q_{13}$',
H='accept|label=$q_{14}$',
))
