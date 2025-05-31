from latextool_basic import *
p = FunctionPlot(domain='0:4000', vars=['n'], height='2.5in')
p.add('abs(0.31415*n**4 + 1000*n**3)', color='red', python=1, 
      pin='below', num_points=1000,
      pin_x=3120, 
      pin_message='|0.31415 n^{4} + 1000n^3|')
p.add('n**4', color='blue', python=1, pin='above left',
      #pin_x=90,
      pin_message='n^4',
      num_points=50, #pin_x=97
)
print (p)
