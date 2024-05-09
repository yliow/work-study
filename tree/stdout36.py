from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(shape='circle',
        yscale=1.3,
        minimum_size='10mm',
        layout='''
             a
                d
                   j
                      m  
        ''',
        a=r'label=\texttt{10}',
        d=r'label=\texttt{18}',
        j=r'label=\texttt{20}',
        m=r'label=\texttt{22}',
        edges='a>d,d>j,j>m',
        ))
