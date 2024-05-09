from latextool_basic import *
p = Plot()

h0 = graph2(xoffset=0,yscale=1, xscale=1,
layout="""
   A 
 B   C
D E G
""",
minimum_size='8mm',
edges='A-B,A-C,B-D,B-E,C-G',
A=r'label=\texttt{10}',
B=r'label=\texttt{5}',
C=r'label=\texttt{7}',
D=r'label=\texttt{2}',
E=r'label=\texttt{1}',
G=r'label=\texttt{5}',
)
p += h0

h1 = graph2(xoffset=7,yscale=1, xscale=1,
layout="""
   A 
 B   C
D E G
""",
minimum_size='8mm',
edges='A-B,A-C,B-D,B-E,C-G',
A=r'label=\texttt{10}',
B=r'label=\texttt{5}',
C=r'label=\texttt{7}',
D=r'label=\texttt{2}',
E=r'label=\texttt{1}',
G=r'label=\texttt{5}',
)
p += h1

print(p)
