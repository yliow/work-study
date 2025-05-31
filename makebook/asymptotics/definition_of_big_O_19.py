from latextool_basic import *
p = FunctionPlot(domain='1:30', vars=['n'])
p.add('3*n**2+5+10*n*sin(n)', color='red', python=1, pin='below', pin_x=17, num_points=100)
p.add('4*n**2', color='blue', python=1, pin='above', num_points=20)
print(p)
