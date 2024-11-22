from math import *
import shutil
import config as con
import attributes as at
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
    i = 1
    for path in con.contents:
        s += r'''
%(include)s
        '''  % {'include':at.include(path)}
    s += r'''
\input{thispostamble.tex}
    '''
    return "main.tex", s

def thispostamble():
    tex = r'''\printindex
\end{document}
    '''
    return "thispostamble.tex", tex

def thispreamble():
    tex = r'''\newcommand\COURSE{%(courses)s}
\newcommand\ASSESSMENT{%(assignment)s}
\newcommand\ASSESSMENTTYPE{Assignment}
\newcommand\POINTS{	textwhite{xxx/xxx}}

\input{myquizpreamble}
    
\input{%(name)s}
\input{thistitle}
\renewcommand\EMAIL{}
\input{\COURSE}
\textwidth=6in

\input{thispackages}
    
    \input{thismacros}

\makeindex
\begin{document}
\topmatter
    ''' % {'assignment': at.assignment_it,
        'courses': at.courses,
        'name':at.name}
    return "thispreamble.tex", tex

def thistitle():
    tex = r'''\renewcommand\TITLE{\ASSESSMENTTYPE \ \ASSESSMENT}
    '''
    return "thistitle.tex", tex

def thismacros():
    tex = ""
    return "thismacros.tex", tex

def thispackages():
    tex = ""
    return "thispackages.tex", tex


