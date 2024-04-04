from latextool_basic import *
print(automata(layout="""
A B
""",
edges="A,$a$,B|B,$a,b$,B",
A="initial|label=$q_0$",
B="accept|label=$q_1$",
))
