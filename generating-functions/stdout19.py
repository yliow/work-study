from latextool_basic import *
plot = Plot()
plot += Rect(0, 0, 12, 2)
plot += Rect(0, 0, 2, 1, background='blue!20!white')
plot += Rect(0, 1, 2, 2, background='blue!20!white')
plot += Rect(7, 0.25, 7, 0.25, label='$n - 2$', linewidth=0)
print(plot)
