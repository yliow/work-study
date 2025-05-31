from latextool_basic import *
from fib_node import node

p = Plot()

d = positions('''
       A  
   B       I
 C   F   G   H
D E     
''', xscale=0.8, yscale=1.1)
edges={
    'A':['B', 'I'],
    'B':['C','F'],
    'C':['D', 'E'],
    'I':['G', 'H'],
}

Graph.r = 0.3

label = {'A':'fib(4)',
         'B':'fib(3)',
         'C':'fib(2)',
         'D':'fib(1)',
         'E':'fib(0)',
         'F':'fib(1)',
         'G':'fib(1)',
         'H':'fib(0)',
         'I':'fib(2)',
         
         }

for k in d:
    x,y = d[k]
    p += node(x=x, y=y,
              label=r'{\footnotesize \texttt{%s}}' % label[k],
              name=k)
   
for k in edges:
    for v in edges[k]:
        p += Graph.edge(names=[k,v])
        
print(p)
