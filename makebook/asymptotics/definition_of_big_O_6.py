from latextool_basic import *
p = FunctionPlot(vars=['n','y'])
p.add('3*n**2 + 5 + 10*n * sin(n)', color='red', python=1, pin='right', pin_x=5)
p.add('50*n', color='blue', python=1, pin='left', num_points=2)
print(p)
