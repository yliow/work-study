import funct
import os

def main():
    s = '''\\input{thispreamble.tex}\n\n\\newcommand\\myincludetex[1]{\\textbox{{\\scriptsize \\texttt{#1}}}\n\n
    \\input{#1}\n\n}\n\n\\newcommand\\myincludesrc[1]{\\textbox{{\\scriptsize \\texttt{#1}}}\n\n
    \\VerbatimInput[fontsize=\\footnotesize,frame=single]{#1}\n\n}\n'''

    for i in config.dir:
        s = s + "\\newpage\n\\input{" + i + '}\n\n'

    s = s + "\\input{thispostamble.tex}\n"
    return "main.tex", s


funct.write(main())

if not(os.path.exists("makefile")):
    funct.write(funct.makefile())

if not(os.path.exists("thismacros")):
    funct.write(funct.thismacros())

if not(os.path.exists("thispackages")):
    funct.write(funct.thispackages())

if not(os.path.exists("thispostamble")):
    funct.write(funct.thispostamble())

if not(os.path.exists("thispreamble")):
    funct.write(funct.thispreamble())

if not(os.path.exists("thistitle")):
    funct.write(funct.thistitle())
