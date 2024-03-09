import glob
from pyutil import *

def check(s):
    # check "\begin{python}"
    # check "section{"
    return

if __name__ == '__main__':
    fs = glob.glob("*.tex")
    for f in fs:
        print(f)
    input("continue? ")
    f = fs[0]
    print("filename:", f)
    input("continue? ")
    s = readfile(f)
    check(s)
