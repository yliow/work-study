from latextool_basic import *

p = Plot()
r0 = Rect(0, 0, 2, 2)
x,y = r0.top()
y += 0.25
t0 = Rect(x, y, x, y, label=r'$\DFA_\Sigma$', linewidth=0)
p += r0
p += t0

r1 = Rect(4, 0, 8, 4)
x,y = r1.top()
y += 0.25
t1 = Rect(x, y, x, y, label=r'$\LANG_\Sigma$', linewidth=0)
p += r1
p += t1

r2 = Rect(4, 0, 5.5, 1.5, background='black!10')
p += r2
x,y = r2.top()
y += 0.25
t2 = Rect(x, y, x, y, label=r'$\Reg_\Sigma$', linewidth=0)
p += t2


x0,y0 = r0.right()
x1,y1 = r1.left()
p += Line(points=[(x0,y0), (x1,y0)], endstyle='>')

print(p)
