from latextool_basic import *
p = Plot()
Graph.r = 0.4
Graph.background = 'white'
p += Graph.node(x=0, y=0, name='1', label='$p$')
p += Graph.node(x=5, y=0, name='2', label='$q$')
p += Graph.arc(names=['1', '2'], label=r'$\texttt{a}, \texttt{b} \rightarrow \texttt{c} $')
print(p)
