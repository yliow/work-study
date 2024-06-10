from latextool_basic import *
p = Plot()
p += Rect(x0=0, y0=0, x1=3, y1=1, label='problem', name='problem')
p += Rect(x0=4, y0=0, x1=8, y1=1, label='recurrence relation', name='recurrence')
p += Rect(x0=9, y0=0, x1=13, y1=1, label='closed form', name='closed form')
p += Line(names=['problem', 'recurrence'], linecolor='blue', endstyle='>')
p += Line(names=['recurrence', 'closed form'], linecolor='blue', endstyle='>')
p += Line(names=['problem', 'closed form'], bend_right='20', linecolor='red', endstyle='>')
print(p)
