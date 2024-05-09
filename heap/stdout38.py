from latextool_basic import *
p = Plot()
edges={20: [10, 5],
10: [ 9, 1],
5: [ 0, 7],
9: [ 2],
}
p += Line(names=[5, 7], linewidth=0.03, endstyle='>',
startstyle='>', linecolor='red', bend_left=60)
drawheap(p, edges, include_array=False)
print(p)
