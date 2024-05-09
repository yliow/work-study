from latextool_basic import *
p = Plot()
DLLNode = DoublyLinkedListNode
x = 0
n5 = DLLNode(x=x, y=0, prev=None, label=5, width=0.6)
p += n5

x += 2
n3 = DLLNode(x=x, y=0, label=3, width=0.6)
p += n3

x += 2
n4 = DLLNode(x=x, y=0, label=4, width=0.6)
p += n4

x += 2
n6 = DLLNode(x=x, y=0, label=6, next=None, width=0.6)
p += n6

p += Pointer(points = [n5[2].center(), n3[0].left()])
p0 = n3[0].center()
p1 = n5[1].top()
p2 = p0[0], p0[1] + 0.75
p3 = p1[0], p2[1]
p += Pointer(points = [p0, p2, p3, p1])

p += Pointer(points = [n3[2].center(), n4[0].left()])
p0 = n4[0].center()
p1 = n3[1].top()
p2 = p0[0], p0[1] + 0.75
p3 = p1[0], p2[1]
p += Pointer(points = [p0, p2, p3, p1])

p += Pointer(points = [n4[2].center(), n6[0].left()])
p0 = n6[0].center()
p1 = n4[1].top()
p2 = p0[0], p0[1] + 0.75
p3 = p1[0], p2[1]
p += Pointer(points = [p0, p2, p3, p1])


print(p)
