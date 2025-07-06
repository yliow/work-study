from latextool_basic import *
p = Plot()
#p += Grid(x0=-3,y0=-10,x1=15,y1=5)

G = Rect(-1, 3, 1, 5, linewidth=0.05, font=r'\huge', label=r'\texttt{G}')
P0 = Rect(-3, -1, -0.5, 1, linewidth=0.05, font=r'\huge', label=r'\texttt{P0}')
P1 = Rect(0.5, -1, 3, 1, linewidth=0.05, font=r'\huge', label=r'\texttt{P1}')
C = Rect(-1, -5, 1, -3, linewidth=0.05, font=r'\huge', label=r'\texttt{C}')

p += Line(points=[(-2,-1),(-2,-2),(2,-2),(2,-1),(2,-2),(0,-2),(C.top())], linewidth=0.05)
p += Line(points=[(-2,-2),(-2,-1)], linewidth=0.05, endstyle='>')
p += Line(points=[(2,-2),(2,-1)], linewidth=0.05, endstyle='>')
p += Line(points=[(-2,1),(-2,2),(2,2),(2,1),(2,1),(2,2),(0,2),(G.bottom())], linewidth=0.05, endstyle='>')

E0 = ellipse(5,0,8,2, linewidth=0.1, label=r'x\_')
E1 = ellipse(9,0,12,2, linewidth=0.1, label=r'x\_')
E2 = ellipse(5,-3,8,-1, linewidth=0.1)
E3 = ellipse(9,-3,12,-1, linewidth=0.1)
E4 = ellipse(7,-6,10,-4, linewidth=0.1)
p += Line(points=[(6.5,1), (6.5,-2), (8.5,-5), (10.5,-2), (10.5,1)], linewidth=0.1)

p += G
p += Line(points=[G.right(),(6.5,1)], linewidth=0.05)
p += Line(points=[G.right(),(10.5,1)], linewidth=0.05)

p += P0
p += Line(points=[P0.bottomright(),(6.5,-2)], linewidth=0.05)

p += P1
p += Line(points=[P1.right(),(10.5,-2)], linewidth=0.05)

p += C
p += Line(points=[C.right(),(8.5,-5)], linewidth=0.05)


p += E0
p += E1
p += E2
p += E3
p += E4

print(p)

