from latextool_basic import *
p = Plot()
d = positions(r'''
     X     b     Y
         e   a
        k l   p    
             f d
              h m
             n o
        ''')

Graph.r = 0.3
Graph.background = 'white'
def n(name, d, v):
    x,y = d[name]
    return Graph.node(x=x, y=y, name=name, label=r'\texttt{%s}' % v)
def blank(name, d):
    x,y = d[name]
    return Graph.node(x=x, y=y, name=name, linewidth=0)

p += blank('X', d)
p += blank('Y', d)
      
p += n('a', d, 10)
p += n('b', d, 4)
p += n('d', d, 20)
p += n('e', d, 2)
p += n('f', d, 17)
p += n('k', d, 0)
p += n('l', d, 3)
p += n('p', d, 18)
p += n('h', d, 19)
p += n('m', d, 26)

for a,b in ['ba','pf','pd',"ap", "be", "ek", "el", 'dh', 'dm']:
    p += Graph.arc(names=[a,b])

print(p)
