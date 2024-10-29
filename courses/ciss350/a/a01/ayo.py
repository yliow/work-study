import config
import os

def main():
    s = "\\input{thispreamble.tex}\n\n\\newcommand\\myincludetex[1]{\\textbox{{\\scriptsize \\texttt{#1}}}\n\n  \\input{#1}\n\n}\n\n\\newcommand\\myincludesrc[1]{\\textbox{{\\scriptsize \\texttt{#1}}}\n\n  \\VerbatimInput[fontsize=\\footnotesize,frame=single]{#1}\n\n}\n"

    for i in config.dir:
        s = s + "\\newpage\n\\input{" + i + '}\n\n'

    s = s + "\\input{thispostamble.tex}\n"
    return "main.tex", s


config.write(main())

if not(os.path.exists("makefile")):
    config.write(config.makefile())

if not(os.path.exists("thismacros")):
    config.write(config.thismacros())

if not(os.path.exists("thispackages")):
    config.write(config.thispackages())

if not(os.path.exists("thispostamble")):
    config.write(config.thispostamble())

if not(os.path.exists("thispreamble")):
    config.write(config.thispreamble())

if not(os.path.exists("thistitle")):
    config.write(config.thistitle())
