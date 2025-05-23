from latextool_basic import *
p = FunctionPlot(domain='0:400', vars=['n'], height='2.5in')
p.add('abs(-3*n**3.5 + 42*n**5/(n**2 + 1))', color='red', python=1, 
      pin='above left', num_points=1000, pin_x=230, 
      pin_message='|-3n^{3.5} + 42n^5/(n^2 + 1)|')
p.add('4*n**3.5', color='blue', python=1, pin='left',
      pin_message='4n^{3.5}',
      num_points=50, pin_x=350
)
print (p)
