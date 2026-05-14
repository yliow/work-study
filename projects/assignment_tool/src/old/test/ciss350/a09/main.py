from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(yscale=0.9,layout='''
   A
  B C
   F G
''',
minimum_size='8mm',
edges='A-B,A-C,C-F,C-G',
A=r'label=\texttt{+}',
B=r'label=\texttt{1}',
C=r'label=\texttt{*}',
F=r'label=\texttt{2}',
G=r'label=\texttt{3}'))

