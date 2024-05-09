from latextool_basic import graph
print(r"""\begin{center}
%s
\end{center}""" % graph(yscale=0.8, layout='''
         Z
       B
     A   E
    C D  
''',
minimum_size='8mm',
edges='Z-B,B-A,A-D,A-C,B-E',
A=r'label=$\alpha$',
B=r'label=$\beta$',
C=r'shape=tree, minimum height=2cm, label=$T_1$',
D=r'shape=tree, minimum height=2cm, label=$T_2$',
E=r'shape=tree, minimum height=2cm, label=$T_3$',
Z=r'shape=None, label=$$',
))
