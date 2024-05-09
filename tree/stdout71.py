from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(yscale=0.8, layout='''
      E
        
     A
   C   B
''',
minimum_size='8mm',
edges='A-B,A-C,E-A',
A=r'label=$\alpha$',
B=r'shape=tree, minimum height=2cm, label=$T_2$',
C=r'shape=tree, minimum height=2cm, label=$T_1+k$',
E=r'shape=None, label=$$',
))
