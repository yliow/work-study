from latextool_basic import *
p = FunctionPlot(domain='3:7', vars=['n'])
p.add('abs(n**5/(1 + n) * sin(1000/n) - 100)', color='red', python=1, 
pin='left', num_points=1000, pin_message='|n^5/(1+n) sin(1000/n) - 100|',
pin_x=6.2)
p.add('n**4', color='blue', python=1, pin='left', num_points=200, pin_x=7)
print(p)
