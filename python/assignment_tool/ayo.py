import funct
import config
import os

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

funct.write(main())

if not os.path.exists("makefile"):
    funct.write(funct.makefile())

if not os.path.exists("thismacros"):
    funct.write(config.thismacros())

if not os.path.exists("thispackages"):
    funct.write(config.thispackages())

if not os.path.exists("thispostamble"):
    funct.write(funct.thispostamble())

if not os.path.exists("thispreamble"):
    funct.write(funct.thispreamble())

if not os.path.exists("thistitle"):
    funct.write(funct.thistitle())
