s = r'''
n = 2
while 1:
    p = 1
    for i in range(1, n):
        p *= (1 - i / 366.0)
    print(n, 1 - p)
    if 1 - p > 0.5:
         break
    n += 1
'''.strip()
f = open('a15245236.py', 'w')
f.write(s)
f.close()
from latextool_basic import *
print(r'{\small %s}' % console(s))
print("and the output")
print(r'{\small %s}' % shell('python a15245236.py'))

