from latextool_basic import graph
print(r"""\begin{center}
%s
\end{center}""" % graph(yscale=0.8, layout='''
       Z
     A
   C   B
      D E 
''',
minimum_size='8mm',
edges='Z-A,A-B,A-C,B-D,B-E',
A=r'label=$\alpha$',
B=r'label=$\beta$',
C=r'shape=tree, minimum height=2cm, label=$T_1$',
D=r'shape=tree, minimum height=2cm, label=$T_2$',
E=r'shape=tree, minimum height=2cm, label=$T_3$',
Z=r'shape=None, label=$$',
))
