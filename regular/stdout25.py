from latextool_basic import *
print(automata(layout="""
A  B
""",
edges="",
A="initial|label=$\{q_0\}$",
B="label=$\{\}$",
))
