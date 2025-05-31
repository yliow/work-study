from latextool_basic import *
p = FunctionPlot(domain='0:10', vars=['n'])
p.add('abs(n**5/(1 + n) * sin(1000/n) - 100)', color='red', python=1, 
      pin='left', num_points=1000, pin_x=9.5,
      pin_message='|n^5/(1 + n) * sin(1000/n) - 100|')
p.add('n**2', color='blue', python=1, pin='left', num_points=2, pin_message='')
print(p)
