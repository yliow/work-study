import latex_fragment as latex
import makefile as make
import config
import os

def write(x):
    name, s = x
    f = open(name, "w")
    f.write(s)
    f.close()

write(latex.main())

if not os.path.exists("makefile"):
    write(make.makefile())

if not os.path.exists("thismacros"):
    write(latex.thismacros())

if not os.path.exists("thispackages"):
    write(latex.thispackages())

if not os.path.exists("thispostamble"):
    write(latex.thispostamble())

if not os.path.exists("thispreamble"):
    write(latex.thispreamble())

if not os.path.exists("thistitle"):
    write(latex.thistitle())
