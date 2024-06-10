from latextool_basic import *
plot = Plot()
plot += Rect(0, 0, 5, 2)
plot += Rect(0, 0, 2, 1, background='blue!20!white')
plot += Rect(0, 1, 2, 2, background='blue!20!white')
plot += Rect(2, 0, 4, 1, background='blue!20!white')
plot += Rect(2, 1, 4, 2, background='blue!20!white')
plot += Rect(4, 0, 5, 2, background='blue!20!white')
print(plot)
