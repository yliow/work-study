from latextool_basic import *
p = Plot()
d = positions(r'''
     X     a     Y
         b   p
        e l f d   
         k   h m
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
p += n('h', d, 19)
p += n('m', d, 26)
p += blank('X', d)
p += blank('Y', d)
p += n('a', d, 10)
p += n('b', d, 2)
p += n('d', d, 20)
p += n('e', d, 0)
p += n('f', d, 17)
p += n('k', d, 3)
p += n('l', d, 4)
p += n('p', d, 18)

for a,b in ['lk', 'pf','pd',"ap", "ab", "be",'bl','dh','dm']:
    p += Graph.arc(names=[a,b])

print(p)
