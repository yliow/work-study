from latextool_basic import *
p = FunctionPlot(domain='1:10', num_points=30, vars=['n'])
p.add('3*n**2', color='blue', python=1, pin='below')
p.add('3*n**2 + 5', color='blue', python=1, pin='above')
print(p)
