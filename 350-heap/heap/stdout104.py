from latextool_basic import *
p = Plot()
h = graph2(yscale=1, xscale=1,
layout="""
        A 
    B       C 
  D   E   F   G
 H I J K L M N
""",
minimum_size='8mm',
edges='A-B,A-C,B-D,B-E,C-G,C-F,D-H,D-I,E-J,E-K,F-L,F-M,G-N',
A=r'label=\texttt{34}',
B=r'label=\texttt{28}',
C=r'label=\texttt{16}',
D=r'label=\texttt{23}',
E=r'label=\texttt{25}',
F=r'label=\texttt{13}',
G=r'label=\texttt{7}',
H=r'label=\texttt{10}',
I=r'label=\texttt{8}',
J=r'label=\texttt{24}',
K=r'label=\texttt{14}',
L=r'label=\texttt{3}',
M=r'label=\texttt{9}',
N=r'label=\texttt{5}',
)
p += h

p += r'\node (proot) at (7,0.5) {\texttt{proot}} ;'
p += r'\path [-triangle 60] (proot) edge[] (A);'

p += r'\node (p0) at (1,-4.5) {\texttt{p0}} ;'
p += r'\path [-triangle 60] (p0) edge[] (D);'

p += r'\node (p1) at (13,-4.5) {\texttt{p1}} ;'
p += r'\path [-triangle 60] (p1) edge[] (G);'

p += r'\node (p) at (13,-1.5) {\texttt{p}} ;'
p += r'\path [-triangle 60] (p) edge[] (G);'

print(p)
