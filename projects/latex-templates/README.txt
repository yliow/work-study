TODO: copy texlive/.../latexyliow -> latex-yliow

ADDED GL to mymath. Need to check all latex.

FOR SOLUTIONS: See projects/solutions/

================================================================================

FOR CRYPTO, .... need to have a way to remove to proof, solution, etc.
Something like:

\begin{forinstructoronly}
This is my proof. Will be removed by some program in make.
\end{forinstructoronly}

================================================================================

TYPES OF QUIZZES
- ciss240: Contains main.pdf and main.txt.
- >=ciss245: submit main.tex

TYPES OF ASSIGNMENT
- a01/
  |
  +- main.tex
  |
  +- main.pdf
  |
  +- q01.tex
  |
  +- q02.tex
  |
  +- a01q01/ - program files
  |
  +- a01q02/ - program files
  
Should latex files be in a01q01, etc.?


- a01/
  |
  +- main.pdf and possibly latex files
  |
  +- a01q01/
  |  |
  |  +- src/ (program source files)
  |  |
  |  +- tex/ (latex files)
  |
  +- a01q02/
  |  |
  |  +- src/ (program source files)
  |  |
  |  +- tex/ (latex files)
  |

-------------------------------------------------------------------------------

quiz/

CASE: Enter answers into latex file main.tex

makequiz.py -- copy files to quiz dir



  Example: The directory organization should be
    ciss101/
      q/
        q0101/
          makefile -- "make" will create q0101.tar.gz
                   -- "make a" will create answers/ from questions/,
                      answers.py, parser.py
          questions/
            makefile -- "make s" creates submit.tar.gz (but alex can do this)
            answers.py -- contains answers, a list of strings of answers
            parser.py -- used by makefile
            answers




project/latex-templates/
    makequiz.py
    quiz/ -- template for quiz directories of courses
    makefile
    questions/ -- template for questions/ 
    answers.py
    parser.py
CASE: Enter answers into latex file main.tex and also write complete code

ciss101/
    a/
        a01/
            makefile
                -- "make" will create a01/ and then a01.tar.gz
                -- "make a" will create answers/ from questions/, answers.py, parser.py
            answers.py
                -- contains answers, a list of strings of answers
            parser.py
                -- used by makefile
                     
            questions/
                makefile -- "make s" creates submit.tar.gz (but alex can do this)
                main.tex
                
            answers/

            a01/
                main.tex
                main.pdf
                makefile
                q01.tex
                q02.tex
                a01q01/
                    main.cpp
                a01q02/
                    main.cpp
                    
OR                        

-------------------------------------------------------------------------------
quiz
        ciss240

        in general

        see math325 ... use parser 
        see ciss362 ... uses quiztools

-------------------------------------------------------------------------------
assignment

-------------------------------------------------------------------------------
book
        thispreamble.tex
        thispostamble.tex
        thispackages.tex
        thismacros.tex
        main.tex

! = hi pri
                                                latest book template
projects/python-c-cpp                           DONE 2022/08/10
projects/ai                                     DONE 2022/08/10
projects/aima-solutions
projects/bioinformatics
projects/bitcoin
projects/graph-theory-bondy-murty               COMBINED 2022/08/10
projects/burton-number-theory-solutions
projects/calculus                               DONE 2022/08/10
projects/chemical-applications-of-group-theory
projects/clr
projects/collatz
projects/compgeom
projects/computer-vision
projects/concurrent-distributed-parallel
projects/convex-optimization
projects/cryptocurrency
projects/d
projects/dalg/doc
projects/degree3poly
projects/design-patterns-IS-THIS-MOVED                  
projects/dft                                    DONE 2022/08/10
projects/egyptian-fractions                     DONE 2022/08/11
projects/embedded-system
projects/fibonacci                              DONE 2022/08/11
projects/flask                                  DONE 2022/08/11
projects/gazebo
projects/googletest
projects/group-representation
projects/harmonic-analysis
projects/here-i-stand                           DONE 2022/08/011
projects/ireland-rosen-2 
projects/laplace-transform
projects/latex/styles <-- mentioned
projects/latex-how-to-add-solutions.tex/ <--???
projects/latex-templates/book                   
projects/latex-test/test-book                   DONE 2022/08/11
projects/latex-test/test-macros-pgf
projects/latex-test/test-mybooktwo
projects/latex-test/tmp
projects/linalg/doc
projects/machine-learning                       !
projects/mdb/book-fragments/posix-file-io
projects/ml                                     !
projects/number-fields-marcus                   DONE 2022/08/12
projects/number-theory                          DONE 2022/08/11
projects/ocaml
projects/odd-ones
projects/ooad
projects/outreach
projects/polya
projects/pygame
projects/python-c-cpp                           DONE 2022/08/10
projects/python-stocks
projects/pythonanywhere
projects/qt
projects/rosen8-solutions                       DONE 2022/08/13
projects/rudin-principles-of-mathematical-analysis
projects/secret-sharing
projects/sipser3                                DONE 2022/08/11
projects/unreal
projects/verilog
projects/word-separation-problem                !

courses/atiyah-macdonald

courses/book/csp                         
courses/book/test

courses/diffeq                           DONE 2022/08/11

courses/ciss350/n/asymptotics            DONE 2022/08/12
courses/ciss350/n/comparison-based-sort  DONE 2022/08/12
courses/ciss350/n/distribution-sort      DONE 2022/08/12
courses/ciss350/n/containers             DONE 2022/08/12
courses/ciss350/n/linkedlist             DONE 2022/08/12
courses/math325/n/tree                   DONE 2022/08/12
courses/ciss350/n/hashtable              DONE 2022/08/12
courses/ciss350/n/heap/                  DONE 2022/08/12

courses/ciss362/n/cfl                    DONE 2022/08/11
courses/math325/n/decidability           DONE 2022/08/11
courses/ciss362/n/languages/             DONE 2022/08/11
courses/math325/n/languages              DONE 2022/08/11
courses/ciss362/n/regular/               DONE 2022/08/11
courses/math325/n/time-complexity/       DONE 2022/08/12
courses/ciss362/n/tm/                    DONE 2022/08/11

courses/ciss380/n/opengl

courses/ciss240/latex

ciss430/a/a06/questions/storage/
ciss430/n/05-storage/book/
ciss430/n/08-normalization/
ciss430/n/bptree/

ciss445/n/53-grammars-3-LL-recursive-descent-parsing/old/parsetrees/

latex/yliow1/preamble/mybookpreamble.tex
compiler/n
cpp/cpp-misc/doc/main.tex:1:\input{mybookpreamble}
cppbook/latex-template/main.tex:9:\input{mybookpreamble.tex}
math325/n/main-heap2.tex:1:\input{mybookpreamble}
math325/n/main-student.tex~:2:\input{mybookpreamble}
math325/n/main.tex:1:\input{mybookpreamble}
math325/n/main.tex~:1:\input{mybookpreamble}
math325/n/thispreamble.tex

courses/ciss451/n/block-ciphers
courses/ciss451/n/classical-cryptography
courses/ciss451/n/cryptographic-hash
courses/ciss451/n/digital-signatures
courses/ciss451/n/ecc
courses/ciss451/n/elementary-number-theory
courses/ciss451/n/information-theory
courses/ciss451/n/introduction
courses/ciss451/n/perfect-security
courses/ciss451/n/rsa
courses/ciss451/student-book
courses/ciss451/student-book-1
courses/ciss451/student-book-1-example-1
ciss451/n/template/  ??????

courses/math325/n/backtrack
courses/math325/n/binomial-heap                 DONE 2022/08/12
courses/math325/n/cantor                        DONE 2022/08/12
courses/math325/n/ciss358
courses/math325/n/correctness
courses/math325/n/counting
courses/math325/n/discrete-probability
courses/math325/n/divide-and-conquer
courses/math325/n/dynamic-programming
courses/math325/n/functions-and-relations
courses/math325/n/generating-functions
courses/math325/n/generating-functions-new ????
courses/math325/n/graph
courses/math325/n/graph-algorithms
courses/math325/n/greedy
courses/math325/n/inc-exc
courses/math325/n/order-stat
courses/math325/n/set
courses/number-theory
courses/putnam
courses/real-analysis               <-- move to projects/calculus

THERE ARE TWO number-theory/ in project/ and courses/
-------------------------------------------------------------------------------
project
