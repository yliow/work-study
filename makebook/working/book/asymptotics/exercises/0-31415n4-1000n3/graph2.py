from latextool_basic import *
p = FunctionPlot(domain='1200:2000', vars=['n'], height='2.5in')
p.add('abs(0.31415*n**4 + 1000*n**3)', color='red', python=1, 
      pin='below right', num_points=20,
      pin_x=1620, 
      pin_message='|0.31415 n^{4} + 1000n^3|')
p.add('n**4', color='blue', python=1, pin='above left', num_points=20,
      pin_x=1700,
      pin_message='n^{4}'
)
print (p)
