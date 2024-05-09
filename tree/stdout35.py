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
          b     d
        e   f h   j
       k l     m  
        ''',
        a=r'label=\texttt{10}',
        b=r'label=\texttt{4}',
        d=r'label=\texttt{18}',
        e=r'label=\texttt{2}',
        k=r'label=\texttt{0}',
        l=r'label=\texttt{3}',
        h=r'label=\texttt{15}',
        j=r'label=\texttt{20}',
        m=r'label=\texttt{17}',
        f=r'label=\texttt{8}',
        edges='a>b,a>d,b>e,b>f,d>h,d>j,e>k,e>l,h>m',
        ))
