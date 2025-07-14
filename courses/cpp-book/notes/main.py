from latextool_basic import *
p = Plot()
s = array(x0=0.5, y0=0.5, width=0.6, height=1.2, xs=['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', r'\textbackslash n', 0, ' ', 3, '.', 1, 4, r'\textbackslash  n', 4, 2, ' ',' ',' ',' ',' ',' ',' ',' '], celllinewidth=0.05)
p.add(s)
p += Rect(13.1, 0.51, 13.7, 1.69, background='black')
#p+= Grid(x0=-1, y0=-2, x1=15, y1=5)
p += Line(points=[(13.45,-1),(13.45,0.5)], linewidth=0.3, endstyle='>')
print(p)

