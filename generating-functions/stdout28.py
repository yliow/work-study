from latextool_basic import *
p = Plot()
p += Rect(0, 0, 12, 2)

p += Rect(0, 0, 1, 2, background='blue!20!white')

p += Rect(0, 0, 1, 2, background='blue!20!white')

p += Rect(1, 0, 3, 1, background='blue!20!white')
p += Rect(1, 1, 3, 2, background='blue!20!white')

p += Rect(3, 0, 4, 2, background='blue!20!white')

print(p)
