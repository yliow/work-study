from latextool_basic import *
p = FunctionPlot(line_width=1, domain='0:10', vars=['n','y'])
p.add('2*n+3', color='red', python=1, pin='below')
p.add('n**2', color='blue', python=1, pin='below', num_points=20)
print(p)
