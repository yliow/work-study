COPIED FROM README.txt
- help Liow make pdfs by:
  1) changing the macros in his .tex files to his newer macros
     a) ex: \myinput{} is changed to \newpage\input{}
     b) \section{} is changed to \sectionthree{}
     c) \begin{python0} , \input{solutions.tex}, and the accompanying macros/code
        to set up solutions that Liow uses
  2) putting python code in a seperate .py file, then writing it to a .tex
     file, using makefile, that will be inputted in the main compiled .tex code
  3) putting questions and answers in a seperate "exercises" directory, so it
     hyperlinks in the pdf. (done through Liow's solutions.py code)
