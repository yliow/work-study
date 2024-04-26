from latextool_basic import *
p = Plot()
p += Rect(x0=-0.05, y0=-0.05, x1=11, y1=11)

REG = Rect(x0=0.0, y0=0.0, x1=1, y1=1, linewidth=0.06, radius=0.2)
p += REG
REG_TEXT = Rect(x0=2, y0=-1.0, x1=4, y1=-0.3, label=r"{\footnotesize T3: Reg, DFA, NFA}", linewidth=0)
p += REG_TEXT
p += Line(points=[REG.right(), REG_TEXT.top()])

p += Rect(x0=0.0, y0=0.0, x1=2,y1=3, radius=0.2)
p += Rect(x0=0.2, y0=3.3, x1=5, y1=3.3, s=r"{\footnotesize DCFL, DPDA}", linewidth=0)

p += Rect(x0=0.0, y0=0.0, x1=3, y1=2, radius=0.2)
p += Rect(x0=3.1, y0=0.4, x1=5.1, y1=0.4, s=r"{\footnotesize LCFL}", linewidth=0)

p += Rect(x0=0.0, y0=0.0, x1=4.5, y1=4.5, linewidth=0.06, radius=0.2)
p += Rect(x0=0.2, y0=4.8, x1=5.5, y1=4.8, s=r"{\footnotesize T2: CFG, CFL, PDA}", linewidth=0)

p += Rect(x0=0.0, y0=0.0, x1=6, y1=6, linewidth=0.06, radius=0.2)
p += Rect(x0=0.2, y0=6.3, x1=5.5, y1=6.3, s=r"{\footnotesize T1: CSG, LBA (LBNTM)}", linewidth=0)

p += Rect(x0=0.0, y0=0.0, x1=7.5, y1=7.5, linewidth=0.06, radius=0.2)
p += Rect(x0=0.2, y0=7.8, x1=5.5, y1=7.8, s=r"{\footnotesize TM-decidable}", linewidth=0)

p += Rect(x0=0.0, y0=0.0, x1=9.0, y1=9.0, linewidth=0.06, radius=0.2)
p += Rect(x0=0.2, y0=9.3, x1=5.5, y1=9.3, s=r"{\footnotesize T0: TM-recognizable, UG}", linewidth=0)


print(p)
