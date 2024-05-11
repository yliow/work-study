from latextool_basic import *
p = Plot()
dfa(p,
        x0=0, y0=0, # coordinates of bottom-left of tape
        body_w=3,
        body_h=2,
        tape=['A','a','a', 'b','b','b','c','c','c','$\BLANK$','$\BLANK$','$\BLANK$'], state='',
        head_index=3,
        vsep=1,  # vertical sep between bottom of tape and top of pda
        hsep=1,  # horizontal sep between right edge of pda and stack
        w=0.6, h=None,
        input_tape_str=False,
        no_draw=False
        )
print(p)
