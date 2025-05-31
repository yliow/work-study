from latextool_basic import *
p = FunctionPlot(domain='1:100', vars=['n'])
p.add('3*n**2', color='blue', python=1, pin='left', num_points=30)
p.add('10 * n * sin(n)', color='blue', python=1, pin='above', num_points=200)
print(p)
