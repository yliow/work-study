from latextool_basic import *
p = Plot()

def arr(x=0, y=0, xs=[]):
    return Array2d(x, y, [xs], width=0.7, height=0.7)
def string(x=0, y=0, label=''):
    label = r'\text{\texttt{%s}}' % label
    return Rect2(x, y, x, y, label=label, linewidth=0)
a = arr(xs=[2,0,3,3,2])
p += a
x, y = a[0][0].left()
p += string(x-0.8, y, 'count')
print(p)