from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(yscale=0.8, layout='''
      E
        
     A
   C   B
  D F
''',
minimum_size='8mm',
edges='A-B,A-C,E-A,C-D,C-F',
A=r'label=$\alpha$',
B=r"shape=tree, label=$T'_3$",
C=r'label=$\beta$',
E=r'shape=None, label=$$',
F=r"shape=tree, label=$T'_2$",
D=r"shape=tree, label=$T'_1$",
))
