import glob
from pyutil import *

def check(s):
    # here is where to check a file for keywords
    for i in s:
        print(i, end = '')
    return

if __name__ == '__main__':
    fs = glob.glob("*.tex")
    i = 0
    for f in fs:
        print(f)
        if input('do you want this file? ') == 'y':
            i = f
            break
    f = i
    s = readfile(f)
    check(s)
