from latextool_basic import *
p = FunctionPlot(domain='0:10', num_points=2, vars=['n','y'])
p.add('2*n + 3', color='red', python=1, pin='below')
print(p)
