from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(yscale=0.8, layout='''
      E
        
     C
   D   A
     F   B
''',
minimum_size='8mm',
edges='E-C,C-D,C-A,A-F,A-B',
A=r'label=$\alpha$',
B=r"shape=tree, label=$T'_3$",
C=r'label=$\beta$',
E=r'shape=None, label=$$',
F=r"shape=tree, label=$T'_2+k$",
D=r"shape=tree, label=$T'_1$",
))