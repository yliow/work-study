"""
for a *.tex file with "\section", do this:

\section{Algorithmic analysis: how fast is an algorithm?}
\begin{python0}
from solutions import *; clear() # -- clear solutions.tex
\end{python0}

...

\newpage
\subsection*{Solutions}
\input{solutions.tex}

"""

import os, glob, re

CLEAR = r'''\begin{python0}
from solutions import *; clear()
\end{python0}'''

SOLUTIONS = r'''\newpage
\subsection*{Solutions}
\input{solutions.tex}'''

paths = glob.glob('*.tex')
for path in paths:
    print(path)
    f = open(path, 'r'); s = f.read(); f.close()
    srch = re.search('\\\section\{[^}]+\}', s)
    if srch != None:
        print()
        print(">>> old s:\n")
        print(s[:200] + " .......... " + s[-100:])
        t = srch.group(0)

        need_to_change = False
        if s.find(CLEAR) == -1:
            need_to_change = True
            print(">>>> ADD CLEAR")
            s = s.replace(t + '\n', t + '\n' + CLEAR + '\n\n')
        if s.find(SOLUTIONS) == -1:
            need_to_change = True
            print(">>>> ADD SOLUTIONS")
            s += '\n' + SOLUTIONS + '\n'
        if need_to_change:
            print(">>> new s:\n")
            print(s[:200] + "....." + s[-100:])
            option = input('add (y/n): ')
            if option in 'yY':
                f = open(path, 'r'); f.write(s); f.close()
        else:
            print(">>>> no change needed")    
