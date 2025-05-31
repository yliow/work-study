from latextool_basic import *
p = FunctionPlot(domain='0:100', vars=['n'], height='2.5in')
p.add('abs(5*n**3*cos(n))', color='red', python=1, 
      pin='above left', num_points=400,
      pin_x=55, 
      pin_message=r'|5n^3 \cos(n)|',
)
p.add('5*n**3', color='blue', python=1, pin='left',
      pin_message='5n^3',
      num_points=20,
      pin_x=80
)
print (p)
