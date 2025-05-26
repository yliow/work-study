from latextool_basic import *
p = FunctionPlot(domain='1:200', vars=['n'])
p.add('3*n**2 + 5 + 10*n * sin(n)', color='red', python=1, pin='left', num_points=200)
p.add('50*n', color='blue', python=1, pin='above', num_points=2)
print(p)
