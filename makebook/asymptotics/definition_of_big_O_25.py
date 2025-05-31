from latextool_basic import *
p = FunctionPlot(domain='0:20', vars=['n'])
p.add('abs(-3*n**2 + 5 - 10*n * sin(n))', color='red', python=1, pin='below', pin_message='|-3n^2+5-10n sin(n)|', pin_x=11.5)
p.add('4*n**2', color='blue', python=1, pin='above', num_points=20)
print(p)
