from latextool_basic import *
print(automata(layout="""
A  B

C  D
""",
edges="A,$a$,B|A,$b$,C|B,$b$,D|B,$a$,A|C,$a$,D|C,$b$,A|D,$a$,C|D,$b$,B",
A='initial|label=$[\ep]$',
B='label=$[a]$',
C='label=$[b]$',
D='accept|label=$[ab]$',
xscale=1.2
))

