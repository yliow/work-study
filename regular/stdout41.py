from latextool_basic import *
print(automata(layout="""
A  B   C  D
""",
edges="A,$a$,B|A,$b$,D|B,$a$,B|B,$b$,C|C,$a$,A|C,$b$,B|D,$a$,B|D,$b$,C",
A='initial|label=$0$',
B='label=$1$',
C='label=$2$',
D='accept|label=$3$',
))
