from math import *
from latextool_basic import *
plot = FunctionPlot()

def c(n):
    return n * (n - 1) * (n - 2) / 6

def f(n):
    return c(n) * (1.0/3)**3 * (2.0/3)**(n - 3)
    
data1 = [(i,f(i)) for i in range(3,20)]
data2 = [(i,0.25) for i in range(0,20)]

plot.add(data1, line_width='1', color='black')
plot.add(data2, line_width='1', color='black')
print(plot)
