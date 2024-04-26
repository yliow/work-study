from latextool_basic import *
print(automata(layout=r"""
C    D    E
""",
C = "label=$p$",
D = "label=new state",
E = "label=$q$",
edges=r"C,$a,b\rightarrow\epsilon\text{ (pop)}$,D|D,$\epsilon,\epsilon\rightarrow c\text{ (push)}$ ,E",
))
