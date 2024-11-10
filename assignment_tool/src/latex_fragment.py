from math import *
import shutil
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

def file_getter(path):
    end = len(path)
    start = end - 1
    
    while start != 0:
        if path[start] == '/':
            return path[start + 1: end]
        start -= 1
    return path[start + 1: end]

def copy_path(path, i):
    
    s = rf"{con.assignment}q{i:0>2}/doc/"
    
    if path[0] == "QUESTION":
        s += rf"q{i:0>2}.tex"
        shutil.copy(path[1], con.newpath + con.assignment + '/' + s)
    elif path[0] == "question":
        q = s + rf"q{i:0>2}.tex"
        shutil.copy(path[1], con.newpath + con.assignment + '/' + q)
        s += rf"q{i:0>2}s.tex"
        shutil.copy(path[1], con.newpath + con.assignment +  '/' +s)
        
    elif path[0] == "latex string":
        return path[1], i
    elif path[0] == "other":
        file_ = file_getter(path[1])
        print(file_)
        s = r"%(a)s/name" %{'a': con.assignment, "name": file_}
        i -= 1
    s = include_(s);
    return s, i + 1

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
        x, i = copy_path(path, i)
        sol = solution(path[1])
        s += r'''
%(solution)s
%(x)s
        
        '''  % {'x':x, 'solution': sol}
    s += r'''
\input{thispostamble.tex}
    '''
    return r"%(path)s%(assignment)s/main.tex"%{'path': con.newpath, 'assignment':con.assignment}, s

def thispostamble():
    tex = r'''\printindex
\end{document}
    '''
    return r"%(path)s%(assignment)s/thispostamble.tex"%{'path' : con.newpath, 'assignment' :con.assignment}, tex

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
    return r"%(path)s%(assignment)s/thispreamble.tex"%{'path' : con.newpath, 'assignment' :con.assignment}, tex

def thistitle():
    tex = r'''\renewcommand\TITLE{\ASSESSMENTTYPE \ \ASSESSMENT}
    '''
    return r"%(path)s%(assignment)s/thistitle.tex"%{'path' : con.newpath, 'assignment' :con.assignment}, tex

def thismacros():
    tex = ""
    return r"%(path)s%(assignment)s/thismacros.tex"%{'path' : con.newpath, 'assignment' :con.assignment}, tex

def thispackages():
    tex = ""
    return r"%(path)s%(assignment)s/thispackages.tex"%{'path' : con.newpath, 'assignment' :con.assignment}, tex

     
    
