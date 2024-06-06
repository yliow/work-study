#!/usr/bin/python

import sys
import os, glob
from pyutil import *

#def readfile(filename):
#    f = open(filename, 'r')
#    s = f.read()
#    f.close()
#    return s

#def writefile(filename, s):
#    f = open(filename, 'w')
#    f.write(s)
#    f.close()

def check():
    """
    check for problems in tex files
    - check for "section{" ... should be "sectionthree{"
    - 
    """
    texs = glob.glob('*.tex')
    
def clear(filename='solutions.tex'):
    writefile(filename, '')
    
def add(label='', s='', filename='solutions.tex', srcfilename=None):
    #
    # If srcfilename is 'answer.tex', this function will basically copy
    # answer.tex to solutions.tex
    #
    # label = "ex:abc" or "prop:abc" or "thm:abc"
    #
    if ':' not in label:
        label = 'ex:%s' % label
    if srcfilename:
        if not srcfilename.endswith('.tex'):
            srcfilename = srcfilename + ".tex"
        s = readfile(srcfilename)
        
    head,tail = label.split(':')
    if head == 'ex':
        typ = 'Exercise'
    elif head == 'prop':
        typ = 'Proposition'
    elif head == 'thm':
        typ = 'Theorem'
    elif head == 'lem':
        typ = 'Lemma'
    elif head == 'cor':
        typ = 'Corollary'
    else:
        typ = '[UNKNOWN]'
    srclabel = r'%s \ref{%s:%s}' % (typ, head, tail)
    sollabel = r'{sol:%s}' % tail

    # if blank no need to add newpage
    t = readfile(filename)
    newpage = r'\newpage'
    #if t.strip() != '':
    #    newpage = ''
    header = ''
    if t.strip() == '':
        header = r'\section*{Solutions}'
        pass
    
    body = r"""
%s
%s
Solution to %s\labeltext{}%s.

%s
""" % (newpage, header, srclabel, sollabel, s)
    
    f = open(filename, 'a')
    f.write(body)
    f.close()

def add_both(todo_fname=None,
             todo_str=None,
             solution_fname=None,
             solution_str=None,
             label=None):
    if not label:
        return r'\mbox{}\\ >>>>> solutions.py error: NO LABEL \mbox{}\\'

    return latex # might be helpful to store in txt file for debugging?

def make_ex(name):
    # 2023/07/11: allow name to be "ex:name" and "prop:name"
    cwd = os.path.split(os.getcwd())[-1]
    if cwd != 'exercises':
        print('cwd is not exercises ... Ctrl-C to halt or press enter to continue: ')
    if ':' not in name:
        name = 'ex:%s' % name
    typ,name = name.split(':')
    if os.path.isdir(name):
        print('dir %s exists ... halting' % name)
    os.system('mkdir %s' % name)
    cwd = os.getcwd()
    os.chdir(name)

    if typ in ['prop', 'thm', 'lem', 'cor']:
        main = r'''
\begin{%(typ)s}
  \label{%(typ)s:%(name)s}
  \input{exercises/%(name)s/question.tex}
\end{%(typ)s}
\proof
Exercise.
\solutionlink{sol:%(name)s}
\qed
\begin{python0}
from solutions import *
add(label="%(typ)s:%(name)s",
    srcfilename='exercises/%(name)s/answer.tex') 
\end{python0}
''' % {'typ':typ, 'name':name}
    else:
        main = r'''
\begin{%(typ)s} 
  \label{%(typ)s:%(name)s}
  \input{exercises/%(name)s/question.tex}
  \solutionlink{sol:%(name)s}
  \qed
\end{%(typ)s} 
\begin{python0}
from solutions import *
add(label="%(typ)s:%(name)s",
    srcfilename='exercises/%(name)s/answer.tex') 
\end{python0}
''' % {'typ':typ, 'name':name}
    writefile('main.tex', main)

    question = r'''\tinysidebar{\debug{exercises/{%(name)s/question.tex}}}''' % {'name':name}
    writefile('question.tex', question)

    answer = r'''\tinysidebar{\debug{exercises/{%(name)s/answer.tex}}}

    Solution not provided.
    ''' % {'name':name}
    writefile('answer.tex', answer)

    makefile = '''
# add this to ../makefile:
# exercises-[name]:
#     (cd exercises/[name] && make)

run: test0.txt plot0.tex
\t$(NOOP)

test0.txt: test0.py
	python test0.py > test0.txt

plot0.tex: plot0.py
	python plot0.py > plot0.tex
'''
    writefile('makefile', makefile)

    os.chdir(cwd)

def prepare_solutions():
    # If "solutions.tex" exsits: add newpage, "Solution" etc to solutions.tex
    # Else: create empty "solutions.tex"
    if has_solutions():
        f = open('solutions.tex', 'r')
        s = f.read()
        f.close()
        #s = r'''\newpage \subsection*{Solutions} ... subsection''' + s
        f = open('solutions.tex', 'w')
        f.write(s)
        f.close()
        #os.system('solutions.tex solutions-done.tex') # ?????????
        os.system('touch solutions.tex')
        pass # the above of adding "Solutions" is done in add
    else:
        clear()

def has_solutions():
    """ Return True is solution.tex exists and not blank """
    if os.path.exists('solutions.tex'):
        f = open('solutions.tex', 'r')
        s = f.read()
        f.close()
        return s.strip() != ''
    else:
        f = open('solutions.tex', 'w')
        f.write('')
        f.close()
        
if __name__ == '__main__':
    pass
    argv1 = sys.argv[1]
    if argv1 == 'clear':
        clear()
    elif argv1 in ['make_ex', 'make-ex']:
        make_ex(sys.argv[2])
    elif argv == 'inputsolutions':
        inputsolutions()
    else:
        print("unknown option", argv1)
