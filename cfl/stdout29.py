from latextool_basic import *
p = Plot()
m = [['$\{B_b,C_b\}$','$\{A_a\}$','$\{A_a\}$','$\{A_a\}$','$\{A_a\}$','$\{B_b,C_b\}$'],
     ['$\emptyset$','$\{C_{(1,2),(1,3)}\}$','$\{C_{(1,3),(1,4)}\}$','$\{C_{(1,4),(1,5)}\}$','$\{S_{(1,5),(1,6)}\}$',''],
     ['$\{A_{(1,1),(2,2)}\}$',r'$\{S_{(1,2),(2,3)}\}$','$\{S_{(1,3),(2,4)}\}$','$\{B_{(2,4),(1,6)}\}$','',''],
     ['$\{C_{(3,1),(1,4)}\}$','$\emptyset$','$\{S_{(1,3),(3,4)}\}$','','',''],
     ['$\{S_{(3,1),(2,4)}\}$','$\{B_{(2,2),(3,4)}\}$','','','',''],
     ['$\{B_{(1,1),(2,5)}$ $S_{(3,1),(3,4)}\}$','','','','',''],
     ]
def getrect():
    i = {0:0}
    width = 2.3
    height = 0.7
    size = len(m)
    def rect(x):
        row, col = i[0] / size, i[0] % size
        if i[0] >= 30:
            i[0] += 1
            return Rect(x0=0, y0=0, x1=width, y1=2 * height,
                            innersep=0.2,
                            s='%s' % x, align='t')
        else:
            i[0] += 1
            return Rect(x0=0, y0=0, x1=width, y1=height,
                            innersep=0.2,
                            s='%s' % x, align='t')
    return rect
    
cyk(p, m, w='baaaab',fontsize='small', rect=getrect())
print(p)
