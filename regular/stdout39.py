from latextool_basic import *
print(automata(layout="""
      C  D
   A 
      G
""",
edges="A,$b$,C|C,$a$,D|D,$b$,A|A,$a$,G|G,$b$,A",
A='initial|accept|label=$q_7$',
C='label=$q_9$',
D='label=$q_{10}$',
G='label=$q_{13}$',
))
