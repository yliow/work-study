from latextool_basic import *
from dllist import *    
p = Plot()
dllist(p, 0, 0, ['?',2,6,4,8,'?'], pheadstr='pheadsentinel', ptailstr='ptailsentinel')
print(p)
