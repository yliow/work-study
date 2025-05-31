from latextool_basic import *
p = FunctionPlot(vars=['n'])
p.add('3*n**2 + 5 + 10*n * sin(n)', color='red', python=1, pin='left')
p.add('3*n**2', color='blue', python=1, pin='below', num_points=20)
print(p)
