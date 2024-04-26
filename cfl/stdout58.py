from latextool_basic import *
print(automata(layout=r"""
A  B
""",
A = "label=$p$",
B = "label=$q$",
edges=r"A,$a, b\rightarrow c$,B",
))
