from latextool_basic import *
p = Plot()
pda_step(p,
         stackvalues0 = ['b','',''],
         tape0 = ['','','a','','','',''],
         state0 = r'$q_5$',
         head_index0 = 2,
         stackvalues1 = [r'\$', '',''],
         tape1 = ['','','a','','','',''],
         state1 = r'$q_2$',
         head_index1 = 2,
        )        
print(p)
