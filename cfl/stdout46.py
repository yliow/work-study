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

x0, y0 = 0, 0
r = pda0(p, x0=x0, y0=y0,
         stackvalues = [], tape = ['a','a','b','b',r'\SPACE'],
         state = r'$q_0$', head_index = 0)
x1,y1 = r.right()
y1 = y0 - 1
p += Line(points=[(x1+0.25,y1),(x1+0.75,y1)],linewidth=0.05,endstyle='>')

x0 = x1 + 1
r = pda0(p, x0=x0, y0=y0,
        stackvalues = [r'\$'], tape = ['a','a','b','b',r'\SPACE'],
        state = r'$q_1$', head_index = 0)
x1,y1 = r.right()
y1 = y0 - 1
p += Line(points=[(x1+0.25,y1),(x1+0.75,y1)],linewidth=0.05,endstyle='>')

x0 = x1 + 1
r = pda0(p, x0=x0, y0=y0,
    stackvalues = ['a', r'\$'], tape = ['a','a','b','b',r'\SPACE'],
    state = r'$q_1$', head_index = 1)
print(p)
