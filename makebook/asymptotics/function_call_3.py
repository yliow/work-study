from latextool_basic import *
p = Plot()

d = positions('''
 A  
 B  
C E 
D    
''', xscale=0.7)
edges={
    'A':['B'],
    'B':['C','E'],
    'C':['D'],
}

Graph.r = 0.3

label = {'A':'f',
         'B':'g',
         'C':'h',
         'D':'i',
         'E':'j',
         }
for k in 'ABCDE':
    x,y = d[k]
    p += Graph.node(x=x, y=y, label=r'\texttt{%s}' % label[k], name=k,
                    linewidth='0.15')
    
for k in edges:
    for v in edges[k]:
        p += Graph.edge(names=[k,v], linewidth='0.15')
        
print(p)
