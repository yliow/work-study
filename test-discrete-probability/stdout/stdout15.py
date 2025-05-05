from math import *
from latextool_basic import *
plot = FunctionPlot()

import scipy.misc
comb = scipy.misc.comb

def B(n, p, k):
    return comb(n, k) * p**k * (1-p)**(n - k)

def f(p):
    return B(7, p, 0) + B(7, p, 1) + B(7, p, 2)
    
data1 = [(i,f(i)) for i in [float(_)/20.0 for _ in range(0,21)]]
data2 = [(i,0.99) for i in [float(_)/20.0 for _ in range(0,21)]]

plot.add(data1, line_width='1', color='black')
plot.add(data2, line_width='1', color='black')
print(plot)
