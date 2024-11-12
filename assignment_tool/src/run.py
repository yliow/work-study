import file_structure as f
import latex_fragment as latex
import makefile as make
import config
import os

def writefile(path, s):
    f = open(path, "w")
    f.write(s)
    f.close()

# makes the file structure
if f.file_struct():
    # create a variable called basepath to
    # be where all files are to be written
    for path, s in [latex.main(),
                    make.makefile(),
                    latex.thismacros(),
                    latex.thispackages(),
                    latex.thispostamble(),
                    latex.thispreamble(),
                    latex.thistitle()]:
        writefile(path, s)
