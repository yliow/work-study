"""
Check latex files
"""
import glob
import re

def readfile(filename):
    f = open(filename, 'r'); s = f.read(); f.close()
    return s
def writefile(filename, s):
    f = open(filename, 'w'); f.write(s); f.close()
    
def unused():
    """
    print x.tex is x.tex is not used (not in input for instance)
    """
    pass

def verbatimfontsize(filename):
    """
    print is Verbatim not using footnotesize
    """
    s = readfile(filename)
    lines = s.split('\n')
    for i,line in enumerate(lines):
        if r'\begin{Verbatim}[' in line and r'fontsize=\footnotesize' not in line:
            print("%s, %s: Verbatim fontsize not footnotesize" % (filename, i + 1))

def pythonprint(filename):
    """
    Check if python file has "print " without parenthesis.
    """
    s = readfile(filename)
    for i,line in enumerate(s.split('\n')):
        if 'print ' in line: print("%s, %s: print with space" % (filename, i))

def pythonfile(filename):
    s = readfile(filename)
    for i,line in enumerate(s.split('\n')):
        if 'file(' in line: print("%s, %s: file( found" % (filename, i))
    
texfiles = glob.glob("*.tex")
texfiles = [_ for _ in texfiles if _ != '_region_.tex']
pyfiles = glob.glob("*.py")
pyfiles = [_ for _ in pyfiles if _ != 'checklatex.py']

for f in texfiles:
    verbatimfontsize(f)

for f in texfiles + pyfiles:
    pythonprint(f)

for f in texfiles + pyfiles:
    pythonfile(f)

    
