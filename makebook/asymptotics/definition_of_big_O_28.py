from latextool_basic import *
p = FunctionPlot(domain='0:10', num_points=2, vars=['n'])
p.add('n**5/(1 + n) * sin(1000/n) - 100', color='red', python=1, pin='below', 
num_points=1000, pin_x=3)
print(p)
