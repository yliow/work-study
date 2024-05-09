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
rects['b'] = node_arr(p, -4, -2, 'b', 2)
rects['c'] = node_arr(p, 0, -2, 'c', 1)
rects['d'] = node_arr(p, 3, -2, 'd', 3)
rects['e'] = node_arr(p, -6, -4, 'e', 2)
rects['f'] = node_arr(p, -3, -4, 'f', 0)
rects['g'] = node_arr(p,  0, -4, 'g', 0)
rects['h'] = node_arr(p,  2, -4, 'h', 1)
rects['i'] = node_arr(p,  5, -4, 'i', 0)
rects['j'] = node_arr(p,  7, -4, 'j', 0)
rects['k'] = node_arr(p, -7, -6, 'k', 0)
rects['l'] = node_arr(p, -5, -6, 'l', 0)
rects['m'] = node_arr(p,  2, -6, 'm', 0)

x0,y0 = rects['a'][3].center()
x1,y1 = rects['b'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')

x0,y0 = rects['a'][4].center()
x1,y1 = rects['c'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')

x0,y0 = rects['a'][5].center()
x1,y1 = rects['d'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')

# b->e
x0,y0 = rects['b'][3].center()
x1,y1 = rects['e'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')
# b->f
x0,y0 = rects['b'][4].center()
x1,y1 = rects['f'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')

# h -> m
x0,y0 = rects['h'][3].center()
x1,y1 = rects['m'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')

# c -> g
x0,y0 = rects['c'][3].center()
x1,y1 = rects['g'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')

# e -> k,l
x0,y0 = rects['e'][3].center()
x1,y1 = rects['k'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')
x0,y0 = rects['e'][4].center()
x1,y1 = rects['l'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')

# d -> h,i,j
x0,y0 = rects['d'][3].center()
x1,y1 = rects['h'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')
x0,y0 = rects['d'][4].center()
x1,y1 = rects['i'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')
x0,y0 = rects['d'][5].center()
x1,y1 = rects['j'][0].topright()
p += Line(points=[(x0,y0), (x0,y0-0.5), (x1,y1)], endstyle='>')

print(p)
