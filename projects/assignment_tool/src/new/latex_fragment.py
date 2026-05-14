from math import *
import shutil
import os


def add_maintex(include_main_tex):
    s = r'''
\input{thispreamble.tex}
\newcommand\myincludetex[1]{\textbox{{\scriptsize \texttt{#1}}}

    \input{#1}
}

\newcommand\myincludesrc[1]{\textbox{{\scriptsize \texttt{#1}}}
    
\VerbatimInput[fontsize=\footnotesize,frame=single]{#1}
}

%s
    
\input{thispostamble.tex}
    ''' % include_main_tex
    return "main.tex", s

def thispostamble():
    tex = r'''\printindex
\end{document}
    '''
    return "thispostamble.tex", tex

def thispreamble(assignment, courses, name):
    tex = r'''\newcommand\COURSE{%(courses)s}
\newcommand\ASSESSMENT{%(assignment)s}
\newcommand\ASSESSMENTTYPE{Assignment}
\newcommand\POINTS{	textwhite{xxx/xxx}}

\input{myquizpreamble}
    
\input{%(name)s}
\input{thistitle}
\renewcommand\EMAIL{}
\input{\COURSE}
\usepackage{import}
\textwidth=6in

\input{thispackages}
\input{thismacros}

\makeindex
\begin{document}
\topmatter
    ''' % {'assignment': assignment,
        'courses': courses,
        'name':name}
    return "thispreamble.tex", tex

def thistitle():
    tex = r'''\renewcommand\TITLE{\ASSESSMENTTYPE \ \ASSESSMENT}
    '''
    return "thistitle.tex", tex

def thismacros():
    return "thismacros.tex", ""

def thispackages():
    return "thispackages.tex", ""


