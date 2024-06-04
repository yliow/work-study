from latextool_basic import *
p = Plot()

def arr(x=0, y=0, xs=[]):
    xs = [[_] for _ in xs]
    return Array2d(x, y, xs, width=0.7, height=0.7)

def string(x=0, y=0, label=''):
    label = r'\text{\texttt{%s}}' % label
    return Rect2(x, y, x, y, label=label, linewidth=0)

def bubble(xs, f):
    n = len(xs)
    #print "xs:", xs
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if f(xs[j]) > f(xs[j + 1]):
                xs[j], xs[j + 1] = xs[j + 1], xs[j]
        #print "xs:", xs

a = ['31','22','02','25','34','41','09']
a = [(_[-1],_) for _ in a]
bubble(a, lambda x:x[0])
a = [_ for __,_ in a] 
a = arr(xs=a)
p += a
x, y = a[0][0].left()
p += string(x-0.3, y, 'x')
print(p)
