from latextool_basic import Rect

H = 0.6
W = 1.5

def node(x, y, label, name, linewidth=None):
    if linewidth:
        return Rect(x0=x, y0=y, x1=x+W, y1=y+H,
                    label=r'\texttt{%s}' % label,
                    name=name, linewidth=linewidth, background='blue!10')
    else:
        return Rect(x0=x, y0=y, x1=x+W, y1=y+H,
                    label=r'\texttt{%s}' % label,
                    name=name, background='blue!10')     
