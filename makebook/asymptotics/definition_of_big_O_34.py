from latextool_basic import *
p = FunctionPlot(vars=['n'], domain='3:7')
p.add('abs(n**5/(1 + n) * sin(1000/n) - 100)', color='red', python=1, 
pin='above', pin_x = 1.6, 
num_points=1000, pin_message=r'|n^5/(1+n) sin(1000/n) - 100|')
p.add('n**4', color='blue', python=1, pin='below', pin_x=2.6, num_points=50)
print(p)
