from latextool_basic import graph
print(r'''
\begin{center}
%s
\end{center}
''' % graph(layout='''
 A
 B
 C
D E
  F
  G
''',
yscale=1.5,
minimum_size='8mm',
edges='A>B,B>C,C>D,C>E,E>F,F>G',
A=r'label=$$',
B=r'label=$$',
C=r'label=$$',
D=r'label=$\texttt{*}$',
E=r'label=$\texttt{*}$',
F=r'label=$\texttt{}$',
G=r'label=$\texttt{*}$',
edge_label={('A','B'):{'label':r'\texttt{c}'},
('B','C'):{'label':r'\texttt{a}'},
('C','D'):{'label':r'\texttt{b}', 'style':'pos=0.8,above,inner sep=3mm,circle'},
('C','E'):{'label':r'\texttt{t}'},
('E','F'):{'label':r'\texttt{c}'},
('F','G'):{'label':r'\texttt{h}'},
#('A','D'):{'label':'a very very long label'},
#('C','E'):{'label':'5', 'style':'pos=0.5,above'},
#('C','F'):{'label':'5', 'style':'pos=0.5,below'},
#('F','G'):{'label':'5', 'style':'pos=0.5,above,inner sep=1mm,circle'},
#('F','H'):{'label':'5', 'style':'pos=0.5,below,inner sep=1mm,circle'},
#('G','I'):{'label':'abcdef', 'style':'sloped'},
},
))
