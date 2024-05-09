from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(yscale=0.8, layout='''
       E
        
     A
   F   B
 C  H
D G 
''',
minimum_size='8mm',
edges='E-A,A-F,A-B,F-C,F-H,C-D,C-G,A-B',
A=r'label=$\alpha$',
B=r"shape=tree, label=$T''_4$",
C=r'label=$\beta$',
E=r'shape=None, label=$$',
F=r"label=$\gamma$",
G=r"shape=tree, label=$T''_2$",
H=r"shape=tree, label=$T''_3$",
D=r"shape=tree, label=$T''_1$",
))
