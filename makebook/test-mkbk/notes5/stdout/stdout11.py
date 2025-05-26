from math import *
from latextool_basic import *
plot = FunctionPlot()

import scipy.special
comb = scipy.special.comb

def B(n, p, k):
    return comb(n, k) * p**k * (1-p)**(n - k)

n = 30
p = 5.0 / 6
data1 = [(k, B(n, p, k)) for k in range(0, n + 1)]

plot.add(data1, line_width='1', color='black')
#plot.add(data2, line_width='1', color='black')
print(plot)
