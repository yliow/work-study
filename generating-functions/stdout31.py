from latextool_basic import *
plot = Plot()
plot += Line(points=[(-1, -1), (1, 1)])
plot += Line(points=[(-1, 0), (1, 0)])
plot += Line(points=[(-1, 1), (2, -1)])
print(plot)
