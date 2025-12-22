from latextool_basic import *
p = Plot(scale=0.85)

codebox = Rect(-10.2, 0, -2.0, 6, linewidth=0.05)

textbox0 = Rect(-8.75, 5.5, -9.0, 5.5, linewidth=0.0, label='\\texttt{void f()}', align='l')
textbox1 = Rect(-9.9, 5, -9.95, 5, linewidth=0.0, label='\\texttt{\{}', align='l')
textbox2 = Rect(-6.0, 4.5, -6.0, 4.5, linewidth=0.0, label='\\texttt{int * p = new int;}', align='l')
textbox3 = Rect(-9.9, 4, -9.95, 4, linewidth=0.0, label='\\texttt{\}}', align='l')
textbox4 = Rect(-8.65, 3, -8.8, 3, linewidth=0.0, label='\\texttt{int main()}', align='l')
textbox5 = Rect(-9.9, 2.5, -9.95, 2.5, linewidth=0.0, label='\\texttt{\{}', align='l')
textbox6 = Rect(-8.75, 2, -8.0, 2, linewidth=0.0, label='\\texttt{...}', align='l')
textbox7 = Rect(-5.25, 1.5, -5.25, 1.5, linewidth=0.0, label='\\texttt{f(); f(); f(); f(); f();}', align='l')
textbox8 = Rect(-8.75, 1, -8.0, 1, linewidth=0.0, label='\\texttt{...}', align='l')
textbox9 = Rect(-9.9, 0.5, -9.95, 0.5, linewidth=0.0, label='\\texttt{\}}', align='l')

execbox = Rect(-10.0, -3, -4.0, -2, linewidth=0.0,
               label='\\EMPHASIZE{Program execution at this point}')
execbox0 = Rect(-10.0, -4, -4.0, -3, linewidth=0.0,
               label='\\EMPHASIZE{(about to call f() a second time)}')

p += execbox
p += execbox0

membox = Rect(0.0, -1.5, 4.0, 5.5, linewidth=0.1)

#markbox = Rect(5.5, -1, 8.25, 2, innersep=0.1, linewidth=0.0, s='this area is still marked as used', align='c')
#p += markbox
fstore = Rect(4.5, -1.5, 8.5, 5.5, linewidth=0.1)
fstorelabel = Rect(6.5, 7, 6.5, 7, linewidth=0.0, label='\\textbf{Free Store}')

fbluebox = Rect(6, 4.5, 7.5, 5, linewidth=0.0, background='blue')
fbox = Rect(0.5, 2.5, 3.5, 4.75, linewidth=0.1)
flabel = Rect(0.5, 5.5, 0.5, 5.5, linewidth=0.0, label='\\textbf{f}')

mbox = Rect(0.5, -1.5, 3.5, 1.25, linewidth=0.1)
mboxlabel = Rect(1.5, 2, 1.5, 2, linewidth=0.0, label='\\textbf{main}')

p += membox

p += fstore
p += fstorelabel
p += fbluebox
p += fbox
p += flabel

p += mbox
p += mboxlabel

p += codebox
p += textbox0
p += textbox1
p += textbox2
p += textbox3
p += textbox4
p += textbox5
p += textbox6
p += textbox7
p += textbox8
p += textbox9

reddot = Circle(x=-9, y=4.5, r=0.2, linecolor='red', background='red')
p += Line(points=[(-9.25, -1.5), (-9, 4.15)], linewidth=0.15, linecolor='red', endstyle='>')
p += reddot

print(p)

