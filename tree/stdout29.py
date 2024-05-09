from latextool_basic import graph
print(r"""\begin{center}
%s
\end{center}""" % graph(yscale=0.8, layout='''
      A
    C   B
''',
minimum_size='8mm',
edges='A-B,A-C',
A=r'label=$\alpha$',
C=r'shape=tree, minimum height=2cm, label=$T_1$',
B=r'shape=tree, minimum height=2cm, label=$T_2$',
))
