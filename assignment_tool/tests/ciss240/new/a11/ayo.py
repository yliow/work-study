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

write(make.makefile())

write(latex.thismacros())

write(latex.thispackages())

write(latex.thispostamble())

write(latex.thispreamble())

write(latex.thistitle())
