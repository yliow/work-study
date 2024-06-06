from latextool_basic import *
plot = Plot()
plot += Rect(0, 0, 2, 1, background='blue!20!white', linewidth=0)
plot += Rect(1, 0, 2, 2, background='blue!20!white', linewidth=0)
plot += Line(points=[(0,0), (2,0), (2,2), (1,2), (1,1), (0,1), (0,0)], linewidth=0.01)
print(plot)
