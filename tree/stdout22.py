from latextool_basic import *
WIDTH = HEIGHT = 0.6 # for main cells
PWIDTH = PHEIGHT = 0.3 # for pointers

def node(x, y, s):
    xs = []
    xs.append(Rect2(x0=x, y0=y, x1=x+WIDTH, y1=y+HEIGHT, label=r'{\texttt{%s}}' % s))
    xs.append(Rect2(x0=x+WIDTH, y0=y, x1=x+2*WIDTH, y1=y+HEIGHT, label=''))
    xs.append(Rect2(x0=x+WIDTH+0.25*WIDTH, y0=y+0.25*HEIGHT, x1=x+2*WIDTH-0.25*WIDTH, y1=y+HEIGHT-0.25*HEIGHT, label=''))
    return xs

def ptrarr(x, y, n):
    xs = []
    for i in range(n):
        xs.append(Rect2(x0=x+PWIDTH*i, y0=y, x1=x+PWIDTH*(i+1), y1=y+PHEIGHT, label=''))
    return xs

def cross(p, r):
    p += Line(points=[r.topleft(), r.bottomright()])
    p += Line(points=[r.topright(), r.bottomleft()])
    
def node_arr(p, x, y, s, n):
    xs = node(x, y, s)
    p += xs[0]; p += xs[1]; p += xs[2]
    x,y = xs[2].bottomleft()
    ys = ptrarr(x + 1, y, n)
    for i in range(n): p += ys[i]
    if n > 0:
        p += Line(points=[xs[2].center(), ys[0].left()], endstyle='>')
    else:
        cross(p, xs[2])
    return xs + ys

p = Plot()

rects = {}
rects['a'] = node_arr(p, 0, 0, 'a', 3)

print(p)
