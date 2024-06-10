from latextool_basic import *
from latexcircuit import *
p = Plot()
Graph.r = 0.4
Graph.background='blue!5'
d = positions('''
A
B
C               D
E         F     G
H     J   T     U     6
I   K N   S   2 V   0 5
L M O P Q R 1 3 W X Y Z 4
''', xscale=0.55)

label = {'A':'$P_1$',
         'B':'$P_1$',
         'C':'$P_1$',
         'D':'$P_{11}$',
         'E':'$P_1$',
         'F':'$P_{12}$',
         'G':'$P_{11}$',
         'H':'$P_1$',
         'I':'$P_1$',
         'J':'$P_{13}$',
         'K':'$P_{14}$',
         'L':'$P_{1}$',
         'M':'$P_{15}$',
         'O':'$P_{14}$',
         'N':'$P_{13}$',
         'P':'$P_{13}$',
         'Q':'$P_{131}$',
         'R':'$P_{12}$',
         'S':'$P_{12}$',
         'T':'$P_{12}$',
         'U':'$P_{11}$',
         'V':'$P_{11}$',
         'W':'$P_{11}$',
         'X':'$P_{113}$',
         'Y':'$P_{112}$',
         'Z':'$P_{111}$',
         '0':'$P_{112}$',
         '1':'$P_{122}$',
         '2':'$P_{121}$',
         '3':'$P_{121}$',
         '4':'$P_{1111}$',
         '5':'$P_{111}$',
         '6':'$P_{111}$',
}
for k in label:
    label[k] = r'{\scriptsize %s}' % label[k]

edges = ['CD', 'HJ', 'IK', 'EF', 'LM', 'HJ', 'PQ', 'Z4', 'S2', 'R1', 'WX', 'V0', 'U6']
    
for k in d:
    x,y = d[k]
    lab = label[k]
    p += Graph.node(x=x, y=y, label=lab, name=k)
    
for e in edges:
    k0,k1 = e
    p += Graph.arc(names=[k0,k1])
    
x,y = d['A']
X = POINT(x=x+14, y=y, r=0, label=r'{\scriptsize beginning}')
p += str(X)

x,y = d['B']
X = POINT(x=x+14, y=y, r=0, label=r'{\scriptsize after 1 month}')
p += str(X)

x,y = d['C']
X = POINT(x=x+14, y=y, r=0, label=r'{\scriptsize after 2 months}')
p += str(X)

x,y = d['E']
X = POINT(x=x+14, y=y, r=0, label=r'{\scriptsize after 3 months}')
p += str(X)

for xs in ['FTSR', 'KO', 'ABCEHIL', 'JNP', '23', 'DGUVW', '0Y', '65Z']:
    xs = list(xs)
    xs = zip(xs[:-1], xs[1:])
    for e in xs:
        k0,k1 = e
        p += Graph.edge(names=[k0,k1])
        
print(p)
