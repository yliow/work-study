from latextool_basic import *
print(automata(layout="""
A
""",
edges=r"A,$(a\rightarrow a, S), (b\rightarrow a, S),(\SPACE\rightarrow \SPACE, S), $,A",
A="initial|accept|label=$q_0$",
))
