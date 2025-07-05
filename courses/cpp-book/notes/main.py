from latextool_basic import *
p = Plot()
p += Grid(x0=-3,y0=-5,x1=3,y1=5)

G = Rect(-1, 3, 1, 5, linewidth=0.05, font=r'\huge', label=r'\texttt{G}')
P0 = Rect(-3, -1, -0.5, 1, linewidth=0.05, font=r'\huge', label=r'\texttt{P0}')
P1 = Rect(0.5, -1, 3, 1, linewidth=0.05, font=r'\huge', label=r'\texttt{P1}')
C = Rect(-1, -5, 1, -3, linewidth=0.05, font=r'\huge', label=r'\texttt{C}')

points_bottom = [(P0.bottom()), (-2, P0.bottomy()), (2, P1.bottomy()), P1.bottom(), (2, P1.bottomy()), (0, -2), (C.top())]

print(points_bottom)

p += Line(points=[(-2,-1),(-2,-2),(2,-2),(2,-1),(2,-2),(0,-2),(C.top())], linewidth=0.05)
p += Line(points=[(-2,-2),(-2,-1)], linewidth=0.05, endstyle='>')
p += Line(points=[(2,-2),(2,-1)], linewidth=0.05, endstyle='>')
p += Line(points=[(-2,1),(-2,2),(2,2),(2,1),(2,1),(2,2),(0,2),(G.bottom())], linewidth=0.05, endstyle='>')


p += G
p += P0
p += P1
p += C
print(p)

