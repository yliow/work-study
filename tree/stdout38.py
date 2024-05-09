from latextool_basic import *
p = Plot()
d = positions(r'''
                   
             a
          b     p
        e   f h   A
       k l     m    
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
p += n('m', d, 17)
p += n('f', d, 8)

for a,b in ['ap', 'hm', 'ab', 'ph', 'pA',
            "be", "bf", "ek", "el"]:
    p += Graph.arc(names=[a,b])

print(p)
