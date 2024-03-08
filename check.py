import glob
from pyutil import *

def check(s):
    return

if __name__ == '__main__':
    fs = glob.glob("*.tex")
    f = fs[0]
    s = readfile(f)
    check(s)
