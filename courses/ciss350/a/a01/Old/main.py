from latextool_basic import *
p = Plot()

p += Rect(x0=0.04, y0=0, x1=7, y1=3, linewidth=0, s = \
r'''\begin{Verbatim}[commandchars=\\\{\}]
                              \textred{\underline{*}}
                    *        ***
            *      ***      *****
      *    ***    *****    *******
  *  ***  *****  *******  *********
************************************
\end{Verbatim}''')

p += Rect(x0=0.03, y0=0.4, x1=7.35, y1=3.04, linewidth=0.01)

d = 0.2435
p += Line(points=[(d,0.4),(d,3.04)], linewidth=0.01)
x = 0.839
p += Line(points=[(x,0.4),(x,3.04)], linewidth=0.01)
x = 1.86
p += Line(points=[(x,0.4),(x,3.04)], linewidth=0.01)
x = 3.27
p += Line(points=[(x,0.4),(x,3.04)], linewidth=0.01)
x = 5.093
p += Line(points=[(x,0.4),(x,3.04)], linewidth=0.01)

p += Line(points=[(0.03,2.94),(6.1,2.94)], linewidth=0.05, startstyle='<', endstyle='>')


print(p)

