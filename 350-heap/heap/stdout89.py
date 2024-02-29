from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(yscale=1, xscale=1,
layout="""
    B        
  D   E      
 H I J K 
P
""",
minimum_size='8mm',
edges='B-D,B-E,D-H,D-I,E-J,E-K,H-P',
A=r'label=\texttt{34}',
B=r'label=\texttt{28}',
D=r'label=\texttt{23}',
E=r'label=\texttt{25}',
H=r'label=\texttt{10}',
I=r'label=\texttt{8}',
J=r'label=\texttt{24}',
K=r'label=\texttt{14}',
P=r'label=\texttt{9}',
))
