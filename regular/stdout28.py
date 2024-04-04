from latextool_basic import *
print(automata(layout="""
A  B
""",
edges="A,$a,b$,B|B,$a,b$,B",
A="initial|label=$\{q_0\}$",
B="label=$\{\}$",
))
