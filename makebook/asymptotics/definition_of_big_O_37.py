from latextool_basic import *
p = FunctionPlot(line_width=1, domain='0:10', vars=['n','y'])
p.add('3*n**2 + 5 + 10*n * sin(n)', color='red', python=1, pin='left')
p.add('30*n', color='blue', python=1, pin='below', num_points=2)
print(p)
