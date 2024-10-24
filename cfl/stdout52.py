from latextool_basic import *
p = Plot()

def pda0(p, x0, y0, stackvalues, tape, state, head_index):
    return pda(p,
           x0=x0,y0=y0,
           stackvalues = stackvalues,
           tape = tape,
           state = state,
           head_index = head_index,
           vsep=0.5, hsep=0.25,
           body_w=1,body_h=0.7,w=0.4,
           )

r = r0 = pda0(p, x0=0, y0=0,
         stackvalues = [], tape = [r'\SPACE' for i in range(5)],
         state = r'$q_0$', head_index = 0)
x0,y0 = r.right()

p += Line(points=[(x0+0.25,y0),(x0+0.75,y0)],linewidth=0.05,endstyle='>')

r = pda0(p, x0=x0+1, y0=0,
        stackvalues = [r'\$'], tape = [r'\SPACE' for i in range(5)],
        state = r'$q_1$', head_index = 0)
print(p)
