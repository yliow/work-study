from latextool_basic import *
p = Plot()

pda(p,
    stackvalues = ['b','',''],
    tape = ['','','a','','','',''],
    state = r'$q_5$',
    head_index = 2,
    vsep=0.5,
    )
print(p)
