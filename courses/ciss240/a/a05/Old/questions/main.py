from latextool_basic import *

p = Plot()
c = RectContainer(x=1, y=1, align='bottom', direction='top-to-bottom')
for row in range(-1, 8):
    c0 = RectContainer(x=1, y=1, align='bottom', direction='left-to-right')
    if row == -1:
        for col in range(-1, 10):
            if col == -1:
                c0 += Rect2(x0=0, y0=0, x1 = 0.6, y1 = 0.6, linewidth=0.0, label = '')
            else:
                c0 += Rect2(x0=0, y0=0, x1 = 0.6, y1 = 0.6, linewidth=0.0, label = r'\texttt{%s}' % col)
    else:
        for col in range(-1, 10):
            if col == -1:
                c0 += Rect2(x0=0, y0=0, x1 = 0.6, y1 = 0.6, linewidth=0.0, label = r'\texttt{%s}' % row)
            else:
                if 1 <= row <= 2 and 2 <= col <= 8 or 5 <= row <= 6 and 4 <= col <= 7:
                    c0 += Rect2(x0=0, y0=0, x1 = 0.6, y1 = 0.6, linewidth=0.05, background='black')
                else:
                    c0 += Rect2(x0=0, y0=0, x1 = 0.6, y1 = 0.6, linewidth=0.05)
    c += c0
    c0.x = c0.x0; c0.y = c0.y0; c0.layout()


p += c
print(p)

