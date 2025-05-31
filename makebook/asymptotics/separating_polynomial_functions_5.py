from latextool_basic import *
p = FunctionPlot(domain='0:100')

p.add('11*x**2', color='red', python=1, pin='below', pin_message='')
p.add('12*x**2 + 2', color='red', python=1, pin='below', pin_message='')
p.add('13*x**2 + 1', color='red', python=1, pin='below', pin_message='')
p.add('14*x**2 + 5*x - 5', color='red', python=1, pin='below', pin_message='')
p.add('15*(x-1)*(x-2) - 10', color='red', python=1, pin='below', pin_message='')

p.add('6*x**3 ', color='green', python=1, pin='below', pin_message='')
p.add('7*x**3 + 3*x**2 - 20*x - 5', color='green', python=1, pin='below', pin_message='')
p.add('8*x**3 +   x**2 - 25*x - 15', color='green', python=1, pin='below', pin_message='')
p.add('9*x**3 - 15*x**2 - 5*x + 1', color='green', python=1, pin='below', pin_message='')
p.add('10*x**3 - 7*x**2 + 5*x - 100', color='green', python=1, pin='below', pin_message='')

p.add('x**4', color='green', python=1, pin='below', pin_message='')
p.add('2*x**4 + x**2 - 20*x - 9', color='blue', python=1, pin='below', pin_message='')
p.add('3*x**4 +   x**3 - 25*x - 1', color='blue', python=1, pin='below', pin_message='')
p.add('4*x**4 - 15*x**2 - 5*x + 1', color='blue', python=1, pin='below', pin_message='')
p.add('5*x**4 - 2*x**2 - 7*x - 100', color='blue', python=1, pin='below', pin_message='')

print(p)
