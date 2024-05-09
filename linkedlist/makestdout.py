"""
create fragments for makefile

"""
start, end = 34, 99

s0 = '\tstdout%s.tex\\'
for i in range(start, end):
    i = str(i).zfill(2)
    t = s0 % (i)
    print(t)

print()
print()
s = 'stdout%s.tex: stdout%s.py\n\tpython stdout%s.py > stdout%s.tex'
for i in range(start, end):
    i = str(i).zfill(2)
    t = s % (i, i, i, i)
    print(t)
