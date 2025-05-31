from latextool_basic import *
p = FunctionPlot(vars=['n'], domain='0:10')
p.add('abs(n**5/(1 + n) * sin(1000/n) - 100)', color='red', python=1, 
pin='above left', num_points=1000, pin_message=r'|(n^5/(1 + n) sin(1000/n) - 100|', pin_x=9)
p.add('n**4', color='blue', python=1, pin='left', num_points=200, pin_x=10)
print(p)
