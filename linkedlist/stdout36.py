from latextool_basic import *

def node(x, y, s):
    c = RectContainer(x=x, y=y)
    c += Rect2(x0=0, y0=0, x1=1.7, y1=0.5, label=r'{\texttt{%s}}' % s)
    return c

p = Plot()
n01 = node(3, 3, '(0,1),3'); n03 = node(9, 3, '(0,3),2')
n20 = node(0, 1, '(2,0),4'); n22 = node(6, 1, '(2,2),9'); n23 = node(9, 1, '(2,3),2')
n30 = node(0, 0, '(3,0),1'); n31 = node(3, 0, '(3,1),1'); n32 = node(6, 0, '(3,2),8')

p += n01; p += n03
p += n20; p += n22; p += n23
p += n30; p += n31; p += n32

p += Line(points=[n01.right(), n03.left()], endstyle='>')
p += Line(points=[n22.right(), n23.left()], endstyle='>')
p += Line(points=[n30.right(), n31.left()], endstyle='>')
p += Line(points=[n31.right(), n32.left()], endstyle='>')
p += Line(points=[n01.bottom(), n31.top()], endstyle='>')
p += Line(points=[n22.bottom(), n32.top()], endstyle='>')
p += Line(points=[n03.bottom(), n23.top()], endstyle='>')
p += Line(points=[n20.right(), n22.left()], endstyle='>')
p += Line(points=[n20.bottom(), n30.top()], endstyle='>')

# row list
r = RectContainer(x=-2, y=2.75, align='left', direction='top-to-bottom')
for i, x in enumerate([1,2,3,4]):
    r += Rect2(x0=0, y0=0, x1=0.5, y1=0.5, label='')
p += r

x,_ = r[0].center(); x += 1; _,y = n01.left()
p += Line(points=[r[0].center(), (x,y), n01.left()], endstyle='>')
p += Line(points=[r[1].topleft(), r[1].bottomright()]) # cross
p += Line(points=[r[1].topright(), r[1].bottomleft()]) # cross
_,y = n20.left()
p += Line(points=[r[2].center(), (x,y), n20.left()], endstyle='>')
_,y = n30.left()
p += Line(points=[r[3].center(), (x,y), n30[0].left()], endstyle='>')

# column list
c = RectContainer(x=4.25, y=4.5, align='bottom')
for i, x in enumerate([1,2,3,4]):
    c += Rect2(x0=0, y0=0, x1=0.5, y1=0.5, label='')
p += c
_,y = c[0].center(); y -= 0.7; x,_ = n20.top();  
p += Line(points=[c[0].center(), (x,y), n20.top()], endstyle='>')
x,_ = n01.top()
p += Line(points=[c[1].center(), (x,y), n01.top()], endstyle='>')
x,_ = n22.top()
p += Line(points=[c[2].center(), (x,y), n22.top()], endstyle='>')
x,_ = n03.top()
p += Line(points=[c[3].center(), (x,y), n03.top()], endstyle='>')
print(p)
