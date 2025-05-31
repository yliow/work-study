from latextool_basic import *
p = FunctionPlot(domain='30:40', vars=['n'], height='2.5in')
p.add('abs(-3*n**3.5 + 42*n**5/(n**2 + 1))', color='red', python=1, 
pin='above', num_points=20, pin_x=33, 
pin_message='|-3n^{3.5} + 42n^5/(n^2 + 1)|')
p.add('4*n**3.5', color='blue', python=1, pin='right', num_points=10,
      pin_x=33,
      pin_message='4n^{3.5}'
)
print (p)
