from latextool_basic import *
p = FunctionPlot(domain='0:400', vars=['n'], height='2.5in')
p.add('abs(20 * n**5 / (n**3 + 1))', color='red', python=1, 
      pin='above left', num_points=1000, pin_x=230, 
      pin_message=r'|20 \frac{n^5}{n^3 + 1}|')
p.add('20*n**2', color='blue', python=1, pin='left',
      pin_message='20n^2',
      num_points=50, pin_x=350
)
print (p)
