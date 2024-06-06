PROJECT: NOTES
yliow home dir                          work study dir             ryan    liow
--------------                          --------------             ------- ------
courses/ciss350/n/heap/                 350-heap/                  done    copied back to courses/ciss350/n/heap/
courses/ciss350/n/hashtable/            350-hashtable/             done    copied back to courses/ciss350/n/hashtable/
courses/math325/n/cantor/               cantor/                    done    copied back to courses/math325/n/cantor/
courses/ciss362/n/regular/              regular/                   done    copied back to courses/ciss362/n/regular/
courses/ciss362/n/cfl/                  cfl/                       done    copied back to courses/ciss362/n/cfl/
courses/ciss362/n/languages/            languages/                 done    copied back to courses/ciss362/n/languages/
courses/ciss362/n/tm/                   tm/                        done    copied back to courses/ciss362/n/tm/
courses/ciss362/n/decidability/         decidability/              done    copied back to courses/ciss362/n/decidability/
courses/ciss350/n/containers/           containers/                done    copied back to courses/ciss350/n/containers/
courses/ciss350/n/distribution-sort/    distribution-sort/         done    copied back to courses/ciss350/n/distribution-sort/
courses/ciss350/n/linkedlist/           linkedlist/                done    copied back to courses/ciss350/n/linkedlist/
courses/ciss350/n/tree/                                                  (this is mostly done)
courses/math325/n/generating-functions/ generating-functions/

projects/latex-templates/             projects/latex-templates/        
courses/ciss240/q/q01*/               courses/ciss240/q/q01*/

-------------------------------------------------------------------------------
PROJECT: LATEX FOR QUIZZES
The goal is to clean up my latex libraries for quizzes.
We'll start off with ciss240 and ciss245.
Look at
-- ciss240/q/q0101/questions/
-- ciss245/q/q2101/questions/
-- projects/latex-templates/quiz/template/questions/
-- /usr/share/texlive/texmf-local/tex/latex/yliow/

ciss240/q/q0101/questions/* are mainly copied from projects/latex-templates/quiz/template/questions/*
Later extra information where added to the this* files in ciss240/q/q0101/questions/*.
This is the same for all other questions/ in all courses.

Ideally
-- ciss240/q/q0101/question/* should be copied
   from projects/latex-templates/quiz/template/questions/ with minimal change.
-- This means that most of the extra stuff (macros) in ciss240/q/q0101/questions should
   be moved to somewhere in /usr/share/texlive/texmf-local/tex/latex/yliow/

-------------------------------------------------------------------------------
PROJECT: update for vm

PROJECT: f36
-- f36 (and further vm) must have the update_vm program in home/student/.

yliow/projects/update_vm/
|
+-- update_vm.py
|           
+-- 0/ (version 0)
    |
    +-- makefile with
    |   -- make build: builds files/*
    |   -- make update: installs files/*
    |
    +-- files/    -- data files to be used by update.py
    |

PROJECT: alex05
-- alex client
-- grader
-- gradereport
===============================================================================
Dr. Liow's notes:

2024/04/11: In some latex file near the top the following

\begin{python0}
  from solutions import *; clear()
\end{python0}

should be

\begin{python0}
from solutions import *; clear()
\end{python0}

i.e., no indentation for the python code.

2024/04/11: Each file has one section. There are several section in closure.tex.
For instance the "Closure: Intersection" section is inside closure.tex. Move
the "Closure: Intersection" content into a separate file named
"closure-intersection.tex". Etc. The table of contents will tell you which one
has to be moved out since every section in the table of contents will have
it's own "debug: [filename]" message.

================================================================================

Ryan Harvey's notes on work-study:

most of the work done here:
- making sure future work-study people have documentation to set their virtual
  machine to work for Liow
- help Liow make pdfs by:
  1) changing the macros in his .tex files to his newer macros
     a) ex: \myinput{} is changed to \newpage\input{}
     b) \section{} is changed to \sectionthree{}
     c) \begin{python0} , \input{solutions.tex}, and the accompanying macros/code
        to set up solutions that Liow uses
  2) putting python code in a seperate individual file, then writing it to a .tex
     file that will be inputted in the main compiled .tex code
  3) putting questions and answers in a seperate "exercises" directory, so it
     hyperlinks in the pdf. (done through Liow's solutions.py code)

check documentation on fedora-installation's README.txt file to update your fedora VM

To set up links through Liow's pdfs to create solutions ...
first go into superuser mode

type in: ln -s /usr/lib/python3.7/site-packages/solutions.py /usr/local/bin/solutions

now the command 'solutions' will work when wanting to link an exercise with it's solutions in Latex.

for example, in directory notes, make a directory named exercises, go into this directory and execute 'solutions make-ex example-0'

cut the exercise from the tex file in the notes directory, and paste it into exercises/example-0/question.tex

this will create a directory for example-0, now in the tex file of where this exercise is, do input{exercises/example-0/main.tex} so a link will be created
