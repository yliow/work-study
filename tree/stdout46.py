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
x,y=d['a']
p += Graph.node(x=x,y=y,name='a',label=r'\texttt{10}',linestyle='dashed')
p += Graph.node(x=x,y=y-0.7,name='aa',label=r'\texttt{8}')
#p += Graph.node(x=x,y=y-1, name='aa', label=r'\texttt{8}',linecolor='white')
#p += Graph.arc(names=['aa','a'], linewidth=0.05)

p += n('b', d, 0)
p += n('d', d, 18)
p += n('p', d, 15)
p += n('e', d, -2)
p += n('k', d, -3)
p += n('l', d, -1)
x,y=d['h']
p += Graph.node(x=x,y=y,name='h',label=r'\texttt{8}',linestyle='dashed')
p += n('m', d, 6)
p += n('f', d, 5)
p += n('n', d, 4)
p += n('o', d, 7)

for a,b in [('A','aa'), ('aa','p'), ('aa','b'),
            "be", "bf", "fd", "fm", "ek", "el", "mn", "mo"]:
    p += Graph.arc(names=[a,b])
for a,b in ["ap", "fh", "hm", "Aa", "ab"]:
    p += Graph.arc(names=[a,b], linestyle='dashed')

p += Graph.arc(names=['h', 'aa'], linewidth=0.2, linestyle='dashed')

print(p)
