from math import *
import shutil
import config as con
import os

# global variable to iterate for each question

def is_latex(path):
    x = path[len(path) - 4:]
    return x == '.tex'

def is_answer(path):
    x = path[len(path) - 5:]
    return x == 's.tex'

def include_latex(path):
    if (is_answer(path)):
        return r'''\myincludetex{%(path)s}''' %{'path':path}
    else:
        return r'''\input{%(path)s}''' %{'path':path}
    return ""

def include_src(path, frame='single', fontsize='\\footnotesize'):
    #src = r'''\VerbatimInput[frame=%(frame)s,font=%(fontsize)s]{%(path)s}
    #''' % {'path':path, 'frame':frame, 'fontsize':fontsize}
    src = r"\myincludesrc{%(path)s}" % {'path':path}
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
    
    if (con.FIRST_FILE_STRUCTURE):
        s = rf"{con.assignment}q{i:0>2}/doc/"
        skel = rf"{con.assignment}q{i:0>2}/"
    
        if path[0] == "QUESTION" or path[0] == "question":
            new_p = s + rf"q{i:0>2}.tex"
            shutil.copy(path[1], con.newpath + con.assignment + '/' + new_p)
            
            os.system("chmod a=r " + con.newpath + con.assignment + "/" + new_p)
            wr = r'''
{    Q%(num)s}. %(q)s''' %{'num':i, 'q': include_(new_p)}
            if path[0] == "question":
                q = 'q' + str(i).zfill(2)
                #file_ = rf"q{i:0>2}s.tex"
                new_p = r"%(s)s%(q)ss.tex"\
                    %{'s':s, 'q':q}
                f = open(con.newpath + con.assignment + '/' + new_p, 'w')
                f.write("")
                f.close()
                #shutil.copy(path[1], con.newpath + con.assignment + '/' + new_p)
                wr += r'''

    \SOLUTION
        
    %(s)s''' %{'s': include_(new_p)}
            return wr, i + 1
        elif path[0] == "skeleton":
            shutil.copy(path[1], con.newpath + con.assignment + '/' + skel + "skel/skeleton.cpp")
            return r"\myincludesrc{%(skel)sskel/skeleton.cpp}" %{'skel' : skel}, i
        elif path[0] == "latex string":
            return path[1], i
        elif path[0] == "other":
            file_ = file_getter(path[1])
        
            s = r"%(a)s/%(name)s" %{'a': con.assignment, "name": file_}
            shutil.copy(path[1], con.newpath + s)
            s = file_
            i -= 1
        s = include_(s);
        return s, i + 1
    else:
        s = rf"{con.assignment}q{i:0>2}/"
        skel = rf"{con.assignment}q{i:0>2}/"
    
        if path[0] == "QUESTION" or path[0] == "question":
            new_p = s + rf"question/doc/q{i:0>2}.tex"
            shutil.copy(path[1], con.newpath + con.assignment + '/' + new_p)

            os.system("chmod a=r " + con.newpath + con.assignment + "/" + new_p)
        
            wr = r'''
{    Q%(num)s}. %(q)s''' %{'num':i, 'q': include_(new_p)}
        
            if path[0] == "QUESTION":
                new_p = r"%(s)sanswer/src/main.cpp"\
                    %{'s':s}
                f = open(con.newpath + con.assignment + '/' + new_p, 'w')
                f.write("")
                f.close()
                #shutil.copy(path[1], con.newpath + con.assignment + '/' + new_p)
                wr += r'''

    \SOLUTION
        
    %(s)s''' %{'s': include_(new_p)}
            if path[0] == "question":
                q = 'q' + str(i).zfill(2)
                #file_ = rf"q{i:0>2}s.tex"
                new_p = r"%(s)sanswer/doc/%(q)ss.tex"\
                    %{'s':s, 'q':q}
                f = open(con.newpath + con.assignment + '/' + new_p, 'w')
                f.write("")
                f.close()
                #shutil.copy(path[1], con.newpath + con.assignment + '/' + new_p)
                wr += r'''

    \SOLUTION
        
    %(s)s''' %{'s': include_(new_p)}
            return wr, i + 1
        elif path[0] == "skeleton":
            shutil.copy(path[1], con.newpath + con.assignment + '/' + skel + "question/skel/skeleton.cpp")
            return r"\myincludesrc{%(skel)squestion/skel/skeleton.cpp}" %{'skel' : skel}, i
        elif path[0] == "latex string":
            return path[1], i
        elif path[0] == "other":
            file_ = file_getter(path[1])
        
            s = r"%(a)s/%(name)s" %{'a': con.assignment, "name": file_}
            shutil.copy(path[1], con.newpath + s)
            s = file_
            i -= 1
        s = include_(s);
        return s, i + 1
    return 0, 0 # failed operation, this should never happen

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
    ''' % {'assignment': con.assignment,
        'courses': con.courses,
        'name':con.name}
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



















    
