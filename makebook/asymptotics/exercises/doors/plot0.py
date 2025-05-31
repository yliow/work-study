import math
from latextool_basic import *

def ln(x):
    return math.log(x, math.e)

plot = FunctionPlot()

# read data from cpp/stdout.txt
def readfile(filename):
    f = open(filename, 'r'); s = f.read(); f.close()
    return s
s = readfile('cpp/stdout.txt')
data = eval('[' + s + ']')
#print(data)
#asd
plot.add(data, legend='time')

def f(x):
    return x * ln(x)

start = data[0][0]
end = data[-1][0]
#print("end:", start, end, start + 1, end + 1)
#asd
C = 1.5e-8 # 1e-8
data1 = [(x * 10**6, C * f(x * 10**6)) for x in range(start//10**6, end//10**6 + 1)]
plot.add(data1, legend='$C n \ln n, C =%s$' % C, color='red')

print(plot)


