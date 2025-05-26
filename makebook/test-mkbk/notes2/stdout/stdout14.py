from math import *
from latextool_basic import *
plot = FunctionPlot()

def c(n):
    return n * (n - 1) * (n - 2) / 6

def f(p):
    return c(10) * p**3 * (1 - p)**(10 - 3)
    
data1 = [(p/20.0, f(p/20.0)) for p in range(0,20)]
data2 = [(p/20.0, 0.25) for p in range(0,20)]

plot.add(data1, line_width='1', color='black')
plot.add(data2, line_width='1', color='black')
print(plot)
