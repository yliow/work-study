from latextool_basic import *
p = Plot()
a = Array2d(0, 0, width=0.6, height=0.6, 
             xs=[['8','7','4','6','3','2','1','0','9']])
p += a
p0 = a[0][7].bottomright(); p0 = (p0[0], p0[1] - 0.2)
p1 = a[0][7].topright(); p1 = (p1[0], p1[1] + 0.2)
p += Line(points=[p0, p1], linewidth=0.1)
p += Rect(x0=0, y0=-1, x1=2, y1=-1, s=r'\texttt{len = 8}', linewidth=0) 
print(p)
