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
         stackvalues = [], tape = ['a','a','b','b',r'\SPACE'],
         state = r'$q_0$', head_index = 0)
x0,y0 = r.right()
p += Line(points=[(x0+0.25,y0),(x0+0.75,y0)],linewidth=0.05,endstyle='>')
r = pda0(p, x0=x0+1, y0=0,
        stackvalues = [r'\$'], tape = ['a','a','b','b',r'\SPACE'],
        state = r'$q_1$', head_index = 0)
x0,y0 = r.right()
p += Line(points=[(x0+0.25,y0),(x0+0.75,y0)],linewidth=0.05,endstyle='>')
r = pda0(p, x0=x0+1, y0=0,
    stackvalues = ['a', r'\$'], tape = ['a','a','b','b',r'\SPACE'],
    state = r'$q_1$', head_index = 1)
x0,y0 = r.right()
p += Line(points=[(x0+0.25,y0),(x0+0.75,y0)],linewidth=0.05,endstyle='>')
r = pda0(p, x0=x0+1, y0=0,
    stackvalues = ['a', 'a', r'\$'], tape = ['a','a','b','b',r'\SPACE'],
    state = r'$q_1$', head_index = 2)

x0,y0 = r.bottomleft()
x1,y1 = r.bottom()
x2,y2 = r0.bottom(); y2 -= 1
p += Line(points=[(x1,y1-0.25),
                  (x1,y1-0.50),
                  (x2,y1-0.50),
                  (x2,y2-0.85)],linewidth=0.05,endstyle='>')
r = pda0(p, x0=0, y0=y2-1.5,
    stackvalues = ['a', r'\$'], tape = ['a','a','b','b',r'\SPACE'],
    state = r'$q_2$', head_index = 2) # 3 problems


print(p)
