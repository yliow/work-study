"""
USAGE:

    python main.py runtime-of-sum-of-squares

        create runtime-of-sum-of-squares
        create runtime-of-sum-of-squares/main.tex
        create runtime-of-sum-of-squares/question.tex
        create runtime-of-sum-of-squares/answer.tex

     python main.py addpath

        add exercises/runtime-of-sum-of-squares/main.tex     (in verb) 
        add exercises/runtime-of-sum-of-squares/question.tex (in verb) 
        add exercises/runtime-of-sum-of-squares/answer.tex   (in verb)

     python main.py delpath

        delete exercises/runtime-of-sum-of-squares/main.tex     (in verb) 
        delete exercises/runtime-of-sum-of-squares/question.tex (in verb) 
        delete exercises/runtime-of-sum-of-squares/answer.tex   (in verb)
"""

BASE = 'exercises'

import sys, os, glob
name = sys.argv[1]

def addpath():
    dirs = [ f.path for f in os.scandir('.') if f.is_dir() ]
    for d in dirs:
        for x in ['main.tex', 'question.tex', 'answer.tex']:
            x = os.path.join(d, x)
            x  = x.replace("./", '')
            print("d:", d, "x:", x)
            path = os.path.join(d, x)
            f = open(x, 'r'); s = f.read(); f.close()
            if not s.find(x):
                print(">>>> old s:\n", s)
                s = r'\verb!exercises/%s!' % x + '\n\n' + s
                print(">>>> new s:\n", s)
                
    sys.exit()

def delpath():
    sys.exit()

def writefile(path, s):
    f = open(path, 'w')
    f.write(s)
    f.close()

def writefile_if_not_exist(path,
                           s,
                           warning='path exists .. not overwritten'):
    if os.path.exists(path):
        print(warning)
    else:
        writefile(path, s)

if name == 'addpath':
    addpath()

if name == 'delpath':
    delpath()
    
if os.path.exists(name):
    print('directory %s already exists ... not created' % name)
else:
    os.system('mkdir %s' % name)

main_tex = r'''\begin{ex}
  \label{ex:%(name)s}
  \input{%(BASE)s/%(name)s/question.tex}
  \mbox{}\\ \\
  \solutionlink{sol:%(name)s}
  \qed
\end{ex}
\begin{python0}
from solutions import *
add(label="ex:%(name)s",
    srcfilename='%(BASE)s/%(name)s/answer.tex') 
\end{python0}                              
''' % {'BASE':BASE, 'name':name}
writefile('%s/main.tex' % name, main_tex)

path = '%s/question.tex' % (name)
writefile_if_not_exist(path,
                       r'\verb!%(BASE)s/%(path)s!' % {'BASE':BASE, 'path':path},
                       warning=r'\verb!%(BASE)s/%(path)s! exists ... not overwritten' % {'BASE':BASE, 'path':path})

path = '%s/answer.tex' % (name)
writefile_if_not_exist(path,
                       r'\verb!%(BASE)s/%(path)s!' % {'BASE':BASE, 'path':path},
                       warning='\verb!%(BASE)s/%(path)s! exists ... not overwritten' % {'BASE':BASE, 'path':path})
