STEP 0.
At the top of a section for latex file add

    \sectionthree{Riemann hypothesis}
    \begin{python0}
    from solutions import *; clear()
    \end{python0}


STEP 1. mkdir exercises/


STEP 2. In exercises/ run the following in bash shell:

     solutions make-ex prop:foobar

solutions.py is script.
For name (i.e., latex reference label), do not use underscore. Use '-' instead.
For instance prop:foobar-1.
If it's an exercise use ex:foobar.
But "ex" is default and can be omitted.

The above will create
   
    exercises/foobar/
    exercises/foobar/main.tex
    exercises/foobar/question.tex
    exercises/foobar/answer.tex 
    exercises/foobar/makefile

This can be used in latex to add latex fragments to a latex file. The main
use case is when the latex fragments are solutions to exercises or proofs.


STEP 3.
In your latex file, insert

    \newpage\input{exercises/foobar/main.tex}


STEP 4.
Modify exercises/foobar/question.tex.


STEP 5.
Modify exercises/foobar/answer.tex.




This requires the following (a counter and a macro): .... IS THIS IN YLIOW?

\newcounter{mylabelcounter}
\makeatletter
\newcommand{\labeltext}[2]{%
#1\refstepcounter{mylabelcounter}%
\immediate\write\@auxout{%
  \string\newlabel{#2}{{1}{\thepage}{{\unexpanded{#1}}}{mylabelcounter.\number\value{mylabelcounter}}{}}%
}%
}
\makeatother

\newcommand\solutionlink[1]{
  (\hyperref[#1]{Go to solution},
  page \pageref{#1})}


USAGE: In natural-numbers.tex:

\section{Natural numbers $\N$}
\begin{python0}
from solutions import *; clear() # -- clear solutions.tex
\end{python0}

Exercise example ...
\begin{ex}
  \label{ex:one-plus-two}
  What is 1 + 2?
  \qed
\end{ex}
\begin{python0}
label = "ex:one-plus-two"
s = r'$1 + 2 = 3$.\qed'
from solutions import *
add(label, s)                              # solution in var s
\end{python0}                              # s is written to solutions.tex

Proof example ...
\begin{prop}\label{prop:1+2=3}
  1 + 2 = 3
\end{prop}
\proof
Exercise.
\solutionlink{sol:1+2=3}
\qed
\begin{python0}
from solutions import *
add(label="prop:1+2=3",
    srcfilename='proofA.tex')              # solution in latex file
\end{python0}                              # proofA.tex written to solutions.tex


\newpage
\subsection*{Solutions}
\input{solutions.tex}                      % input solutions.tex
