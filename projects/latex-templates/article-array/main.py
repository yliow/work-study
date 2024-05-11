from latextool_basic import *
p = Plot()
s = chunkedarray(cellwidth=0.6,
                 cellheight=0.6,
                 arr=[3*[''] + [1,6,7,3,4,9,2,5,8] + 5*['']],
                 celllabels = [('start',  3, -1),
                               ('pivot',  6, -1),
                               ('end',   12, -1),
                               ('i',      4,  +1),
                               ('j',     10,  +1),
                              ]
)
p.add(s)
print(p)

