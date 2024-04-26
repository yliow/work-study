from latextool_basic import *
p = Plot()

pda(p,
    stackvalues = ['a','\$'],
    tape = ['a','b','a','a',r'\SPACE',r'\SPACE',r'\SPACE'],
    state = r'$q_0$',
    head_index = 0,
    body_w = 3,
    body_h = 2,
    vsep = 1,
    hsep = 1,
    input_tape_str=True,
    stack_str=True,
    )
print(p)
