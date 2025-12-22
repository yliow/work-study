from latextool_basic import *
p = Plot()
#p += Grid(x0=0,y0=-4,x1=10,y1=4)
D = '''
Program execution in
this block and looks for
i. Program will keep
looking in the next outer
block until it's found or
if not, we have an error
'''
code(p, D)
p += Rect(7,-3,13,3,linewidth=0.15)
p += Rect(7.5,-2.5,12.5,0.1,linewidth=0.15)
p += Rect(8.5,0.5,11.5,2,linewidth=0.05)
p += Rect(8.5,-2,11.5,-0.5,linewidth=0.05)
#p += Rect(8.25,-1.45,8.25,-1.45,linewidth=0,label=r'i')
p += Rect(8.25,1.3,8.25,1.3,linewidth=0,label=r'i')
p += Circle(x=10,y=-1.2,r=0.5, linecolor='red',background='red')
p += Line(points=[(10,-1.2),(10,0.3)],endstyle='>',linewidth=0.1,linecolor='red',linestyle='dashed')
print(p)

