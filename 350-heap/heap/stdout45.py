  from latextool_basic import *
  p = Plot()
  edges={'34':['28','16'],
  '28':['23','25'],
  '16':['13','7'],
  '23':['10','8'],
  '25':['24','14'],
  '13':['3','11'],
  '7':['5','4'],
  '10':['9'],
  }
  drawheap(p, edges, node_hsep=0.2,
  include_array=False)
  print(p)
