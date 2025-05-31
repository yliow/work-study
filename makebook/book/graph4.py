from latextool_basic import *
p = FunctionPlot(domain='0:100', vars=['n'], height='2.5in')
p.add('7^8', color='red', python=1, 
      pin='above', num_points=2,
      pin_x=55, 
      pin_message=r'|5n^3 \cos(n)|',
)
p.add('7^8', color='blue', python=1, pin='below',
      pin_message='7^8',
      num_points=2,
      pin_x=80
)
print (p)
