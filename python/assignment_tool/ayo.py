import funct
import config
import os

def write(x):
    name, s = x
    f = open(name, "w")
    f.write(s)
    f.close()

def main():
    s = r'''
\input{thispreamble.tex}

\newcommand\myincludetex[1]{\textbox{{\scriptsize \texttt{#1}}}


    \input{#1}

}

\newcommand\myincludesrc[1]{\textbox{{\scriptsize \texttt{#1}}}


    \VerbatimInput[fontsize=\footnotesize,frame=single]{#1}

}
    '''

    for path in config.dir:
        x = funct.include_(path)
        s += r'''
\newpage
%(x)s
        
        '''  % {'x':x}
    s += r'''
\input{thispostamble.tex}
    '''
    return "main.tex", s

write(main())

if not os.path.exists("makefile"):
    write(funct.makefile())

if not os.path.exists("thismacros"):
    write(config.thismacros())

if not os.path.exists("thispackages"):
    write(config.thispackages())

if not os.path.exists("thispostamble"):
    write(funct.thispostamble())

if not os.path.exists("thispreamble"):
    write(funct.thispreamble())

if not os.path.exists("thistitle"):
    write(funct.thistitle())
