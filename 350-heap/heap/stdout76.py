from latextool_basic import *
p = Plot()
a = Array2d(0, 0, width=0.6, height=0.6, 
             xs=[['4','3','2','0','1','6','7','8','9']])
p += a
p0 = a[0][4].bottomright(); p0 = (p0[0], p0[1] - 0.2)
p1 = a[0][4].topright(); p1 = (p1[0], p1[1] + 0.2)
p += Line(points=[p0, p1], linewidth=0.1)
p += Rect(x0=0, y0=-1, x1=2, y1=-1, s=r'\texttt{len = 5}', linewidth=0) 
print(p)
