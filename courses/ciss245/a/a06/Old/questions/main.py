from latextool_basic import *
p = Plot()
t0_label = Rect(x0=-0.5, y0=0.5, x1=0.5, y1=1.5, linewidth=0.0, label=r"\texttt{t0}")
t0 = array(x0=0.5, y0=0.5, width=2, height=1, xs=[5,18,0])
main_label = Rect(x0=-0.5, y0=3.0, x1=0.5, y1=3.5, linewidth=0.0, label=r"\texttt{main}")
main = Rect(x0=-0.5, y0=-1.0, x1=7.0, y1=3.0, linewidth=0.05)
p.add(main_label)
p.add(main)
p.add(t0_label)
p.add(t0)

print(p)

