PROJECT: NOTES
                                                                   (Put "work" or "done")
yliow home dir                          work study dir             ryan  robert  nasser      liow
--------------                          --------------             ----  ------  ------      ----
courses/ciss350/a/a01                   courses/ciss350/a/a01                                               
courses/ciss350/a/a02                   courses/ciss350/a/a02                                               
courses/ciss350/a/a03                   courses/ciss350/a/a03                                               

courses/ciss240/a/a01                   courses/ciss240/a/a01             work                               
courses/ciss240/a/a02                   courses/ciss240/a/a02             work
courses/ciss240/a/a03                   courses/ciss240/a/a03
courses/ciss240/a/a04                   courses/ciss240/a/a04             work
courses/ciss240/a/a05                   courses/ciss240/a/a05             work
courses/ciss240/a/a06                   courses/ciss240/a/a06             work
courses/ciss240/a/a07                   courses/ciss240/a/a07             work
courses/ciss240/a/a08                   courses/ciss240/a/a08
courses/ciss240/a/a09                   courses/ciss240/a/a09
courses/ciss240/a/a10                   courses/ciss240/a/a10
courses/ciss240/a/a11                   courses/ciss240/a/a11
courses/ciss240/a/a12                   courses/ciss240/a/a12

courses/ciss358/a/a02                   courses/ciss358/a/a02

Comments for ciss145:
* At top of documents, change "Python Programming Part 1 v0.2" to "Python Programming Part 1 v0.3"

>>>> RESTRUCTURE TO MATCH 240: watch out ... renumber of some files to match number of 240 notes.

                                                                                       ryan       liow
courses/ciss145/n                       STEP 1 - update to py3 using f31.         --------   -------
                                        ciss145/n/00-frontmatter                  done       done.
                                        ciss145/n/01-print-string                            done
                                        
                                        ciss145/n/02-int-values-03-int-variables             | TO COMPBINE
                                        ciss145/n/05_integers                     done       |

                                        ciss145/n/04-floating-point-numbers

                                        ciss145/n/06_branch                       done
                                        ciss145/n/08-if-part2                     done
                                        
                                        ciss145/n/06_strings                      done       
                                        ciss145/n/07_loop                         done

                                        ciss145/n/10-for-loops-part1.odt
                                        ciss145/n/11-for-loops-part2.odt
                                        
                                        ciss145/n/07_loop_while                   done       | TO COMBINE
                                        ciss145/n/12-while-loops                             |
                                        
                                        ciss145/n/08_pygame1                      done
                                        ciss145/n/09_pygame2                      done
                                        ciss145/n/09_pygame3                      done
                                        ciss145/n/09_pygame4                      done


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
