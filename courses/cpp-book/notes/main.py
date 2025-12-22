from latextool_basic import *
p = Plot()

p += Rect(-1, -2, 15, 5, linewidth=0.1)

p += Rect(1, 3, 5, 4, label='3.14')
p += Rect(1, 1, 5, 2)
p += Rect(1, -1, 5, 0)

p += Line(points=[(3, 1.75), (9, 3.5)],
          linewidth=0.1, endstyle='>')
p += Line(points=[(3, -0.5), (6.5, -0.5), (6.5, 1.25), (5, 1.25)],
          linewidth=0.1, endstyle='>')

p += Rect(0.5, -0.5, 0.5, -0.5, label='p', linewidth=0.0)
############

p += Rect(9, 3, 13, 4, label='2.718')
p += Rect(9, 1, 13, 2)
p += Rect(9, -1, 13, 0)

p += Line(points=[(11, 1.75),  (4, 3.5)],
          linewidth=0.1, endstyle='>')
p += Line(points=[(11, -0.5), (14.5, -0.5), (14.5, 1.25), (13, 1.25)],
          linewidth=0.1, endstyle='>')

p += Rect(8.5, -0.5, 8.5, -0.5, label='q', linewidth=0.0)

print(p)

