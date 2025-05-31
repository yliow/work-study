from latextool_basic import *
p = FunctionPlot(domain='0:10')

p.add('x**2', color='red', python=1, pin='below', pin_message='')
p.add('x**2 + 2', color='red', python=1, pin='below', pin_message='')
p.add('x**2 + 1', color='red', python=1, pin='below', pin_message='')
p.add('x**2 + 5*x - 5', color='red', python=1, pin='below', pin_message='')
p.add('(x-1)*(x-2) - 10', color='red', python=1, pin='below', pin_message='')

p.add('x**3 ', color='green', python=1, pin='below', pin_message='')
p.add('x**3 + 3*x**2 - 20*x - 5', color='green', python=1, pin='below', pin_message='')
p.add('x**3 +   x**2 - 25*x - 15', color='green', python=1, pin='below', pin_message='')
p.add('x**3 - 15*x**2 - 5*x + 1', color='green', python=1, pin='below', pin_message='')
p.add('x**3 - 7*x**2 + 5*x - 100', color='green', python=1, pin='below', pin_message='')

p.add('x**4', color='green', python=1, pin='below', pin_message='')
p.add('x**4 + x**2 - 20*x - 9', color='blue', python=1, pin='below', pin_message='')
p.add('x**4 +   x**3 - 25*x - 1', color='blue', python=1, pin='below', pin_message='')
p.add('x**4 - 15*x**2 - 5*x + 1', color='blue', python=1, pin='below', pin_message='')
p.add('x**4 - 2*x**2 - 7*x - 100', color='blue', python=1, pin='below', pin_message='')

print(p)
