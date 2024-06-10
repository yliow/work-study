from latextool_basic import *
plot = Plot()
plot += Rect(0, 0, 12, 2)
plot += Rect(0, 1, 2, 2, background='blue!20!white')
plot += Circle(x=1.5, y=1.5, r=0.2, background='black')
plot += Rect(0, 0, 2, 1, background='blue!20!white')
plot += Circle(x=0.5, y=0.5, r=0.2, background='black')
print(plot)
