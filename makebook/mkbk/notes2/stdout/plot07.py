from latextool_basic import *
p = Plot()
p += Rect(x0=0, y0=0,    x1=1.25, y1=1.0,      linewidth=0, name='1', label=r'$\ONE$')
p += Rect(x0=0, y0=-0.5, x1=1.25, y1=0.5,   linewidth=0, name='6', label=r'$\SIX$')

y = -1.7
p += Rect(x0=0, y0=y-1.0, x1=1.25, y1=y-0,        linewidth=0, name='2', label=r'$\TWO$')
p += Rect(x0=0, y0=y-1.5, x1=1.25, y1=y-0.5,     linewidth=0, name='3', label=r'$\THREE$')
p += Rect(x0=0, y0=y-2.0, x1=1.25, y1=y-1,   linewidth=0, name='4', label=r'$\FOUR$')
p += Rect(x0=0, y0=y-2.5, x1=1.25, y1=y-1.5, linewidth=0, name='5', label=r'$\FIVE$')

p += Rect(x0=4, y0=-1.25 + 1, x1=5,   y1=-0.75 + 1,  linewidth=0, name='p', label=r'$1/6$')

#p += r'\node [ellipse, draw=blue, fit=(1) (2) (3), line width=0.05cm, inner sep=0.1cm] (good) {};'
#p += r'\node [ellipse, draw=red, fit=(4) (5) (6), line width=0.05cm, inner sep=0.1cm] (bad) {};'

p += r'\node [ellipse, draw=blue, fit=(1) (6), line width=0.05cm, inner sep=0.1cm] (good) {};'
p += r'\node [ellipse, draw=red, fit=(2) (3) (4) (5), line width=0.05cm, inner sep=0.1cm] (bad) {};'

p += r'\node [ellipse, draw=black, fit=(good) (bad), line width=0.05cm, inner sep=0.1cm] {};'

p += r'\node [ellipse, draw=black, fit=(p), line width=0.05cm, inner sep=0.5cm] {};'

for i in range(1, 7):
    p += Line(names=['%s' % i, 'p'], endstyle='>')

p += Rect(x0=4, y0=-4 + 1, x1=5,   y1=-3.5 + 1, linewidth=0,  name='13', label=r'\textblue{$1/3$}')
p += Rect(x0=4, y0=-4.5 + 1, x1=5,   y1=-4 + 1, linewidth=0,  name='23', label=r'\textred{$2/3$}')
p += r'\node [ellipse, draw=black, fit=(13) (23), line width=0.05cm, inner sep=0.4cm] {};'

p += Line(names=['good', '13'], endstyle='>', linecolor='blue')
p += Line(names=['bad', '23'], endstyle='>', linecolor='red')

print(p)
