from latextool_basic import *
p = FunctionPlot(vars=['n'], domain='0:1000', num_points=2)
p.add('10*n', color='red', python=1)
p.add('10*n + 10', color='blue', python=1)
p.add('10*n + 50', color='green', python=1)
print(p)
