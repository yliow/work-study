from latextool_basic import *
p = FunctionPlot(domain='1:20', vars=['n'])
p.add('10 * n', color='blue', python=1, pin='above', num_points=2, pin_x=11)
p.add('10 * n * sin(n)', color='blue', python=1, pin='left', pin_x=17, num_points=150)
print(p)
