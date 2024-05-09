"""
create fragments for makefile

"""
start, end = 56, 112

s0 = '\tstdout%s.tex\\'
for i in range(strat, end):
    i = str(i).zfill(2)
    t = s0 % (i)
    print(t)

print()
print()
s = 'stdout%s.tex: stdout%s.py\n\tpython stdout%s.py > stdout%s.tex'
for i in range(56, 112):
    i = str(i).zfill(2)
    t = s % (i, i, i, i)
    print(t)
