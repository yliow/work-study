from latextool_basic import *
p = FunctionPlot(domain='1:3', vars=['n'], height='2.5in')
p.add('abs(7*n**4 + 20)', color='red', python=1, 
      pin='above left', num_points=20,
      pin_x=1.6, 
pin_message='|7n^4 + 20|')
p.add('8*n**4', color='blue', python=1, pin='right', num_points=20,
      pin_x=1.7,
      pin_message='8n^{4}'
)
print (p)
