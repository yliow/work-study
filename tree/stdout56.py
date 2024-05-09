from latextool_basic import Plot, array
p = Plot()
s = array(x0=0.5, y0=0.5, width=0.8, height=0.8, xs=[0,2,3,4,6,8,9,10,12,15,17,18,19,20,22])
p.add(s)
print(p)
