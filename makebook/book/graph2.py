from latextool_basic import *
p = FunctionPlot(domain='0:800', vars=['n'], height='2.5in')
p.add('abs(n**4 - 1234*n**3)', color='red', python=1, 
      pin='above left', num_points=20,
      pin_x=500, 
      pin_message='|n^{4} - 1234n^3|')
p.add('n**4', color='blue', python=1, pin='right', num_points=20,
      pin_x=500,
      pin_message='n^{4}'
)
print (p)
