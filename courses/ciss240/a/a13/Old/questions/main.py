from latextool_basic import *
p = Plot()

c = RectContainer(x=1, y=1, align='bottom', direction='top-to-bottom')
for row in range(10):
    c0 = RectContainer(x=1, y=1, align='bottom', direction='left-to-right')
    for col in range(10):
        val = 10 * row + col
        if (row == 0 and col < 2) or (val % 2 == 0 and val != 2) or \
           (val % 3 == 0 and val != 3) or (val % 5 == 0 and val != 5) or \
           (val % 7 == 0 and val != 7):
            c0 += Rect2(x0=0, y0=0, x1 = 1.6, y1 = 0.6, linewidth=0.02,
                        background='black!20!white',
                        label = r'$%s$' % val)
        else:
            c0 += Rect2(x0=0, y0=0, x1 = 1.6, y1 = 0.6, linewidth=0.02,
                        label = r'$%s$' % val)
    c += c0
    c0.x = c0.x0; c0.y = c0.y0; c0.layout()

p += c
print(p)

