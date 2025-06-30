from latextool_basic import *
p = Plot()
p += Grid(x0=-5, y0=-7, x1=12, y1=5)
D = '''





for (         ;                ;                )








true



false





'''.strip()

p += Line(points=[(2.1, -0.6),(4.2, -0.6)] , linewidth=0.1, linecolor='red', endstyle='>', bend_right=60)
p += Line(points=[(-2.3, -7.6),(-0.2, -7.6)] , linewidth=0.1, linecolor='red', endstyle='>')
p += Line(points=[(-2.3, -6.7),(-2.3, -7.6)] , linewidth=0.1, linecolor='red')
p += Line(points=[(10.7, -6.7),(-2.3, -6.7)] , linewidth=0.1, linecolor='red')
p += Line(points=[(10.7, -5.65), (10.7, -6.7)] , linewidth=0.1, linecolor='red')
p += Line(points=[(10, -5.65),(10.7, -5.65)] , linewidth=0.1, linecolor='red')
p += Line(points=[(8, -0.6),(5.6, -0.6)] , linewidth=0.1, linecolor='red', endstyle='>', bend_left=40)
p += Line(points=[(-0.7, -4.5),(1.6, -4.5)] , linewidth=0.1, linecolor='red', endstyle='>')
p += Line(points=[(7.5, -4.6),(8.6, -0.6)] , linewidth=0.1, linecolor='red', endstyle='>', bend_right=30)
p += Line(points=[(-0.7, -5.65),(10, -5.65)] , linewidth=0.1, linecolor='red', endstyle='>')
p += Line(points=[(-0.7, -3.4),(-0.7, -5.65)] , linewidth=0.1, linecolor='red')
p += Line(points=[(5, -3.4),(-0.7, -3.4)] , linewidth=0.1, linecolor='red')
p += Line(points=[(5, -0.6),(5, -3.4)], linewidth=0.1, linecolor='red')
p += Line(points=[(-1.2, -1.5),(1.9, -0.6)] , linewidth=0.1, linecolor='red', endstyle='>', bend_right=60)
p += Line(points=[(-2.3, -1.5),(-1.2, -1.5)] , linewidth=0.1, linecolor='red', endstyle='>')
p += Line(points=[(-2.3, 1.1),(-2.3, -1.5)] , linewidth=0.1, linecolor='red')
p += Line(points=[(11, 1.1),(-2.3, 1.1)] , linewidth=0.1, linecolor='red')
p += Line(points=[(11, 2.1),(11, 1.1)] , linewidth=0.1, linecolor='red')
p += Line(points=[(10, 2.1),(11, 2.1)] , linewidth=0.1, linecolor='red')

p += Rect(-1.2, 1.6, 10, 3, linewidth=0.1)
p += Rect(1.1, -0.6, 2.7, 0.2, linewidth=0.1)
p += Rect(3.5, -0.6, 5.8, 0.2, linewidth=0.1)
p += Rect(7.5, -0.6, 9.5, 0.2, linewidth=0.1)
p += Rect(-1.2, -6.3, 10, 0.6, linewidth=0.1)
p += Rect(1.6, -4.9, 7.5, -4.3, linewidth=0.1)
p += Rect(-0.2, -8.5, 10.4, -7.1, linewidth=0.1)

code(p, D)

print(p)

