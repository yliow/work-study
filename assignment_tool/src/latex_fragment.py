from math import *
import config as con

# global variable to iterate for each question
question_iterator = 1

def is_question(path):
    a = path[0] == 'a'
    b = path[3] == 'q'
    c = path[1:3].isdigit() and path[4:6].isdigit()
    return a and b and c

def is_latex(path):
    x = path[len(path) - 4:]
    return x == '.tex'

def include_latex(path):
    tex = ""
    global question_iterator
    if (is_question(path)):
        tex += r"{Q%(q)s}. " % {'q': question_iterator}
        question_iterator += 1
    tex += r'''\input{%(path)s}''' %{'path':path}
    return tex

def include_src(path, frame='single', fontsize='\\footnotesize'):
    src = r'''\VerbatimInput[frame=%(frame)s,font=%(fontsize)s]{%(path)s}
    ''' % {'path':path, 'frame':frame, 'fontsize':fontsize}
    return src

def include_(path):
    if is_latex(path):
        return include_latex(path)
    else:
        return include_src(path)

def solution(path):
    if path == 'sln':
        return r'\SOLUTION'
    elif path == 'nln':
        return r'\newpage'
    return ''
    
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

    for path in con.dir:
        x = include_(path[0])
        sol = solution(path[1])
        s += r'''
%(solution)s
%(x)s
        
        '''  % {'x':x, 'solution': sol}
    s += r'''
\input{thispostamble.tex}
    '''
    return r"%(assignment)s/main.tex"%{'assignment':con.assignment}, s

def thispostamble():
    tex = r'''\printindex
\end{document}
    '''
    return r"%(assignment)s/thispostamble.tex"%{'assignment':con.assignment}, tex

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
    ''' % {'assignment': con.assignment,
        'courses': con.courses,
        'name':con.name}
    return r"%(assignment)s/thispreamble.tex"%{'assignment':con.assignment}, tex

def thistitle():
    tex = r'''\renewcommand\TITLE{\ASSESSMENTTYPE \ \ASSESSMENT}
    '''
    return r"%(assignment)s/thistitle.tex"%{'assignment':con.assignment}, tex

def thismacros():
    tex = ""
    return r"%(assignment)s/thismacros.tex"%{'assignment':con.assignment}, tex

def thispackages():
    tex = ""
    return r"%(assignment)s/thispackages.tex"%{'assignment':con.assignment}, tex

     
    
