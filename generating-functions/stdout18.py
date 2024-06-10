from latextool_basic import *
plot = Plot()
plot += Rect(0, 0, 12, 2)
plot += Rect(0, 0, 1, 2, background='blue!20!white')
plot += Rect(6.5, 0.25, 6.5, 0.25, label='$n - 1$', linewidth=0)
print(plot)
