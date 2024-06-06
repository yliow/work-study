from latextool_basic import execute, console
s = r'''
from latextool_basic import *
print(automata(layout="""
A      B
""",
edges=r"A,$\begin{bmatrix}0\\0\\0 \end{bmatrix},\begin{bmatrix}0\\1\\1 \end{bmatrix},\begin{bmatrix}1\\0\\1 \end{bmatrix}$,A"+\
r"|A,$\begin{bmatrix}1\\1\\0\end{bmatrix}$,B"+\
r"|B,$\begin{bmatrix}0\\1\\0\end{bmatrix},\begin{bmatrix}1\\0\\0\end{bmatrix},\begin{bmatrix}1\\1\\1\end{bmatrix}$,B"+\
r"|B,$\begin{bmatrix}0\\0\\1\end{bmatrix}$,A"+\
r"",
A="initial|accept|label=carry=0",
B="label=carry=1",
))
'''
print(console(s.strip()))
execute(s)

