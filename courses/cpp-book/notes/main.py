from latextool_basic import *
p = Plot()
#p += Grid(x0=-2,y0=-5, x1=10, y1=3)
R0 = Rect(6, -2, 15, 0.1, label =r'To make the first dimension dynamic.', linewidth=0.1, linecolor='red')
R1 = Rect(6, -4, 15, -2, label =r'To make the second dimension dynamic', linewidth=0.1, linecolor='red')
R2 = Rect(6, -6.1, 15, -4.1, label =r'To make the value in the 2-d array dynamic', linewidth=0.1, linecolor='red')
L0 = Line(points=[R0.left(),(3.05,-1),(3.05,0.8)], linewidth=0.1, linecolor='red', endstyle='>')
L1 = Line(points=[R1.left(),(2.5, R1.centery()),(2.5, float(R1.centery()) + 3.8)], linewidth=0.1, linecolor='red', endstyle='>')
L2 = Line(points=[R2.left(),(2, R2.centery()),(2,float(R2.centery()) + 5.9)], linewidth=0.1, linecolor='red', endstyle='>')
textbox = Rect(0, 0, 4, 2, label = r'\huge\texttt{Int *** a}', linewidth=0)

p += R0
p += R1
p += R2
p += L0
p += L1
p += L2
p += textbox

print(p)

