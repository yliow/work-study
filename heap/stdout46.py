from latextool_basic import *
p = Plot()
d = positions("""
      A 
   B     C
 D   E F   G
H I J
""",xscale=0.5)
for k,(x, y) in d.items():
    p += Graph.node(x=x, y=y, name=k)
for e in ["AB", "AC", "BD", "BE", "CF", "CG", "DH", "DI", "EJ"]:
    e = [e[0],e[1]]
    p += Graph.edge(names=e)

x0,y0 = d['H']
x1,y1 = x0-0.5, y0+0.5
x2,y2 = x0-0.5, y0-0.5

x3,y3 = d['J']
x4,y4 = x3+0.5, y3+0.5
x5,y5 = x3+0.5, y3-0.5

p += Rect(x0=x2, y0=y2, x1=x4, y1=y4, linecolor='red') 
print(p)
