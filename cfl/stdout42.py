from latextool_basic import *
p = Plot()
Graph.r = 0.4
Graph.background = 'white'
p += Graph.node(x=0, y=0, name='1', label='$q_5$')
p += Graph.node(x=5, y=0, name='2', label='$q_2$')
p += Graph.arc(names=['1', '2'], label=r'$\texttt{a}, \texttt{$\ep$} \rightarrow \texttt{\$} $')
print(p)
