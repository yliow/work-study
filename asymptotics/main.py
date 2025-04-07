from latextool_basic import *
p = FunctionPlot(line_width=1, domain='0:1000', vars=['n','y'])
p.add('40000', color='red', python=1, pin='above right', num_points=2)
p.add('n**2/10', color='green', python=1, pin='above left', num_points=8)
p.add('n * sin(n)', color='blue', python=1, pin='above right', num_points=40)
print (p)

