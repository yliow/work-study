from latextool_basic import *
plot = Plot()
plot += Rect(0, 0, 5, 2)
plot += Rect(0, 0, 1, 2, background='blue!20!white')
plot += Rect(1, 1, 3, 2, background='blue!20!white')
plot += Rect(1, 0, 3, 1, background='blue!20!white')
plot += Rect(3, 0, 4, 2, background='blue!20!white')
plot += Rect(4, 0, 5, 2, background='blue!20!white')
print(plot)
