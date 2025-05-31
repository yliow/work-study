from latextool_basic import *
p = FunctionPlot(vars=['n'], domain='0:10', num_points=2)
p.add('n', color='red', python=1)
p.add('10*n', color='blue', python=1)
p.add('100*n', color='green', python=1)
print(p)
