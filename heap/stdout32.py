from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(yscale=1, xscale=1,
layout="""
   A 
     C
    F G
   H I
""",
minimum_size='8mm',
edges='A-C,C-G,C-F,F-H,F-I',
A=r'shape=None,label=\texttt{}',
B=r'label=\texttt{5}',
C=r'label=$\alpha$',
D=r'label=\texttt{2}',
E=r'label=\texttt{1}',
F=r'label=$\beta$',
G=r'shape=tree,label=$T_3$',
H=r'shape=tree,label=$T_1$',
I=r'shape=tree,label=$T_2$',
))
