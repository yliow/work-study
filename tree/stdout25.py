from latextool_basic import *
p = Plot(xscale=0.5)  
d = positions('''
             a
         b   c   d
        e f  g h i j
       k l     m  
       ''')
edges = {'a':['b','c','d'],
  'b':['e','f'],
  'c':['g'],
  'd':['h','i','j'],
  'e':['k','l'],
  'h':['m'],
}
for k in d.keys():
    x,y = d[k]
    p += Graph.node(x=x, y=y, r=0.3, label=r'$%s$' % k, name=k)

for k,v in edges.items():
    for w in v:
        p += Graph.arc(names=[k, w])
print(p)    
