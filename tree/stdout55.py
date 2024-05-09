from latextool_basic import *
p = Plot()
d = positions(r'''
                   
              a
          b       p
        e   f   h   A
       k l n o m q r s   
        ''')

Graph.r = 0.3
Graph.background = 'white'
def n(name, d, v):
    x,y = d[name]
    return Graph.node(x=x, y=y, name=name, label=r'\texttt{%s}' % v)
      
p += n('A', d, 20)
p += n('a', d, 10)
p += n('b', d, 4)
p += n('p', d, 18)
p += n('e', d, 2)
p += n('k', d, 0)
p += n('l', d, 3)
p += n('h', d, 15)
p += n('m', d, 12)
p += n('f', d, 8)
p += n('n', d, 6)
p += n('o', d, 9)
p += n('q', d, 17)
p += n('r', d, 19)
p += n('s', d, 22)

for a,b in ['ap', 'hm', 'ab', 'ph', 'pA','Ar','As',
            "be", "bf", "ek", "el", 'fo', 'hq', 'fn']:
    p += Graph.arc(names=[a,b])

print(p)
