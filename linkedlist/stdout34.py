from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(yscale=0.8,xscale=0.7,layout='''
       A
   B       C
 D   E   F   G
H I J K L M
''',
minimum_size='7mm',
edges='A-B,A-C,B-D,B-E,C-F,C-G,D-H,D-I,E-J,E-K,F-L,F-M',
A=r'label=\texttt{-}',
B=r'label=\texttt{+}',
C=r'label=\texttt{*}',
D=r'label=\texttt{-}',
E=r'label=\texttt{*}',
F=r'label=\texttt{/}',
G=r'label=\texttt{6}',
H=r'label=\texttt{0}',
I=r'label=\texttt{1}',
J=r'label=\texttt{2}',
K=r'label=\texttt{3}',
L=r'label=\texttt{4}',
M=r'label=\texttt{5}',
))
