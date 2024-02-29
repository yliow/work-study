from latextool_basic import *
print(r"""
\begin{center}
%s
\end{center}
""" % graph(yscale=1, xscale=1,
layout="""
      A 
   B     C
 D   E F   G
H I J
""",
minimum_size='8mm',
edges='A-B,A-C,B-D,B-E,C-G,C-F,D-H,D-I,E-J',
A=r'label=',
B=r'label=',
C=r'label=',
D=r'label=',
E=r'label=',
F=r'label=',
G=r'label=',
H=r'label=',
I=r'label=',
J=r'label=',
))
