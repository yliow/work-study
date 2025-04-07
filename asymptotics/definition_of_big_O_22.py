from latextool_basic import *
p = FunctionPlot(line_width=1, width='5in', height='3in', domain='1:30')
p.add('3*x**2 + 5 + 10*x * sin(x)', color='red', python=1, pin='below', 
pin_x=17, num_points=100,
pin_message='|3n^2 + 5 + 10n sin(n)|'
)
p.add('4*x**2', color='blue', python=1, pin='above', num_points=20,
pin_message='4|n^2|')
print(p)
