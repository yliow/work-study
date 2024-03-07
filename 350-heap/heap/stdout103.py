from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(yscale=1, xscale=1,
layout="""
        A 
    B       C 
  D   E   F   G
 H I J K L M 
""",
minimum_size='8mm',
edges='A-B,A-C,B-D,B-E,C-G,C-F,D-H,D-I,E-J,E-K,F-L,F-M',
A=r'label=\texttt{34}',
B=r'label=\texttt{28}',
C=r'label=\texttt{16}',
D=r'label=\texttt{23}',
E=r'label=\texttt{25}',
F=r'label=\texttt{13}',
G=r'label=\texttt{7}',
H=r'label=\texttt{10}',
I=r'label=\texttt{8}',
J=r'label=\texttt{24}',
K=r'label=\texttt{14}',
L=r'label=\texttt{3}',
M=r'label=\texttt{9}',
))
