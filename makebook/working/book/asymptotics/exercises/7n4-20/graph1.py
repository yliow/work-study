from latextool_basic import *
p = FunctionPlot(domain='0:100', vars=['n'], height='2.5in')
p.add('abs(7*n**4 + 20)', color='red', python=1, 
      pin='below right', num_points=1000, pin_x=70, 
      pin_message='|7n^4 + 20|')
p.add('8*n**4', color='blue', python=1, pin='above left',
      pin_x=90,
      pin_message='8n^4',
      num_points=50, #pin_x=97
)
print (p)
