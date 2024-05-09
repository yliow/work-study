from latextool_basic import *
p = Plot()
d = positions(r'''
     X     a     Y
         b   p
        e q f d   
       l    
      n k      
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
p += n('a', d, 18)
p += n('b', d, 10)
p += n('d', d, 20)
p += n('e', d, 4)
p += n('f', d, 19)
p += n('k', d, 3)
p += n('l', d, 2)
p += n('p', d, 26)
p += n('n', d, 0)
p += n('q', d, 17)

for a,b in ['el','pd','bq','ln', 'lk', 'pf',"ap", "ab", "be",]:
    p += Graph.arc(names=[a,b])

print(p)
