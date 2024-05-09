from latextool_basic import *
print(r'''
\begin{center}
%s
\end{center}
''' % graph(layout='''
 A
 B
''',
yscale=1.5,
minimum_size='8mm',
edges='A>B',
A=r"label=",
B=r"label=\texttt{*}",
edge_label={('A','B'):{'label':r'\texttt{h}'},
},
))
