from latextool_basic import *
p = Plot()
d = positions(r'''
                   A
                a   
          b       p
        e    f    
       k l d   h
              m
             n o
        ''')

Graph.r = 0.3
Graph.background = 'white'
def n(name, d, v):
    x,y = d[name]
    if name == 'A':
        y -= 0.6
    return Graph.node(x=x, y=y, name=name, label=r'\texttt{%s}' % v)
      
p += n('A', d, 20)
#p += n('a', d, 10)
x,y=d['a']
p += Graph.node(x=x,y=y,name='a',label=r'\texttt{10}')
p += Line(points=[(x-0.2,y-0.2),(x+0.2,y+0.2)], linewidth=0.1)
p += Graph.node(x=x,y=y-1, name='aa', label=r'\texttt{0}',linecolor='white')
p += Graph.arc(names=['aa','a'], linewidth=0.05)

#p += n('b', d, 0)
x,y=d['b']
p += Graph.node(x=x,y=y,name='b',label=r'\texttt{0}', linestyle='dashed')

#p += n('d', d, 18)
p += n('e', d, -2)
p += n('k', d, -3)
p += n('l', d, -1)
#p += n('h', d, 8)
#p += n('m', d, 6)
#p += n('f', d, 5)
#p += n('n', d, 4)
#p += n('o', d, 7)
p += n('p', d, 15)

for a,b in ['ae', "Aa", "ap", "ek", "el"]:
    p += Graph.arc(names=[a,b])
for a,b in ['ab','be']:
    p += Graph.arc(names=[a,b], linestyle='dashed')

print(p)