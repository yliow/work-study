from latextool_basic import *
p = Plot()
p += Rect(0, 0, 13, 6, linewidth=0.05)
p += Rect(1, 3, 4, 4, linewidth=0.05, label='4')
p += Rect(4, 3, 8, 4, linewidth=0.05, label='2')
p += Rect(8, 3, 12, 4, linewidth=0.05, label='42')
p += Rect(0.5, 3.5, 0.5, 3.5, linewidth=0, label='a')
p += Rect(0.5, 2, 0.5, 2, linewidth=0, label='x')
p += Rect(1, 1.5, 4, 2.5, linewidth=0.05, label='4')

p += Rect(8, 7, 12, 8, linewidth=0.05, linecolor='red', label='This is a[0]')
p += Rect(8, 6, 12, 7, linewidth=0.05, linecolor='red', label='This is a[1]')
p += Rect(8, 5, 12, 6, linewidth=0.05, linecolor='red', label='This is a[2]')

p += Line(points=[(8, 7.5), (3, 4)], linecolor='red', linewidth=0.05, endstyle='>')
p += Line(points=[(8, 6.5), (6, 4)], linecolor='red', linewidth=0.05, endstyle='>')
p += Line(points=[(10.5, 5), (10, 4)], linecolor='red', linewidth=0.05, endstyle='>')
print(p)

