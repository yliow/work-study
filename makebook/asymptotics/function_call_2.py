from latextool_basic import *
p = Plot()

d = positions('''
 A   a   V   f   F 
 B   b   W   g   G 
C E c e X Z h j H J
D   d   Y   i   I  
''', xscale=0.7)
edges={
    'A':['B'],
    'B':['C','E'],
    'C':['D'],
    #
    'a':['b'],
    'b':['c','e'],
    'c':['d'],
    #
    'V':['W'],
    'W':['X','Z'],
    'X':['Y'],
    #
    'f':['g'],
    'g':['h','j'],
    'h':['i'],
    #
    'F':['G'],
    'G':['H','J'],
    'H':['I'],
}

Graph.r = 0.3

label = {'A':'f',
         'B':'g',
         'C':'h',
         'D':'i',
         'E':'j',
         #
         'a':'f',
         'b':'g',
         'c':'h',
         'd':'i',
         'e':'j',
         #
         'V':'f',
         'W':'g',
         'X':'h',
         'Y':'i',
         'Z':'j',
         #
         'f':'f',
         'g':'g',
         'h':'h',
         'i':'i',
         'j':'j',
         #
         'F':'f',
         'G':'g',
         'H':'h',
         'I':'i',
         'J':'j',
         }
for k in 'ABCDEfghijFGHIJabcdeVWXYZ':
    x,y = d[k]
    if k in 'AfghiFGJabVWX':
        p += Graph.node(x=x, y=y, label=r'\texttt{%s}' % label[k], name=k,
                        linewidth='0.15')
    else:
        p += Graph.node(x=x, y=y, label=r'\texttt{%s}' % label[k], name=k)

for k in edges:
    for v in edges[k]:
        if [k,v] in [['f','g'],
                     ['g','h'],
                     ['h','i'],
                     ['F','G'],
                     ['G','J'],
                     ['a','b'],
                     ['V','W'],
                     ['W','X'],
                     ]:
            p += Graph.edge(names=[k,v], linewidth='0.15')
        else:
            p += Graph.edge(names=[k,v])
        
print(p)
