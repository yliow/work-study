from latextool_basic import *
p = Plot()
d = positions(r'''
           A
          a   
         b p
          e    f    
         k l d   h
              m
             n o
        ''', yscale=0.7)

Graph.r = 0.3
Graph.background = 'white'
def n(name, d, v):
    x,y = d[name]
    return Graph.node(x=x, y=y, name=name, label=r'\texttt{%s}' % v)
      

p += n('A', d, 20)
p += n('a', d, 10)
p += n('b', d, 5)
#p += n('d', d, 18)
p += n('e', d, 8)
p += n('k', d, 6)
p += n('l', d, 9)
p += n('p', d, 15)

for a,b in ["Aa", "ap", "ab", "be", "ek", "el"]:
    p += Graph.arc(names=[a,b])

print(p)
