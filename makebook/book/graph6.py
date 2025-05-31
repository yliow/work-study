from latextool_basic import *
p = FunctionPlot(domain='0:1000000000000000000', vars=['n'])
p.add('abs(20 * n**5 / (n**3 + 1) + 5 * n**3 * cos(n) + 7**8)', color='red', python=1, 
      pin='above', num_points=400,
      pin_x=70, 
      pin_message=r'|20n^5 /(n^3 + 1) + 5n^3 \cos(n) + 7^8|',
)
p.add('7**8 * n**3', color='blue', python=1, pin='above left',
      pin_message='7^8 n^3',
      num_points=20,
      pin_x=70,
)
print (p)
