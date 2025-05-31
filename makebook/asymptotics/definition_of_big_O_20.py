from latextool_basic import *
p = FunctionPlot(line_width=1, width='5in', height='3in', domain='1:20')
p.add('abs(3*x**2 + 5 + 10*x * sin(x))', color='red', python=1, pin='below', pin_message='|3*x^2+5+10x sin(x)|', pin_x=12, num_points=200)
p.add('4*x**2', color='blue', python=1, pin='above', num_points=20)

p = FunctionPlot(domain='1:20', vars=['n'])
p.add('3*n**2+5+10*n*sin(n)', color='red', python=1, pin='below', pin_x=17, num_points=100)
p.add('4*n**2', color='blue', python=1, pin='above', num_points=20)

print(p)
