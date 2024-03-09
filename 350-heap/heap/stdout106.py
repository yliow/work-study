from latextool_basic import *
p = Plot()
h = graph2(yscale=1, xscale=1,
layout="""
        A 
    B       C 
  D   E   F   G
 H I J K L M N O
P
""",
minimum_size='8mm',
edges='A-B,A-C,B-D,B-E,C-G,C-F,D-H,D-I,E-J,E-K,F-L,F-M,G-N,G-O,H-P',
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
O=r'label=\texttt{4}',
P=r'label=\texttt{8}',
)
p += h

p += r'\node (proot) at (8,0.5) {\texttt{proot}} ;'
p += r'\path [-triangle 60] (proot) edge[] (A);'

p += r'\node (p0) at (1,-5.5) {\texttt{p0}} ;'
p += r'\path [-triangle 60] (p0) edge[] (H);'

p += r'\node (p1) at (15,-5.5) {\texttt{p1}} ;'
p += r'\path [-triangle 60] (p1) edge[] (O);'

p += r'\node (p) at (1,-2.5) {\texttt{p}} ;'
p += r'\path [-triangle 60] (p) edge[] (H);'

print(p)
