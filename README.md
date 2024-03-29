# ryan-harvey-ws
# work-study

# most of the work done here:
- making sure future work-study people have documentation to set their virtual machine to work for Liow
- help Liow make pdfs by:
 1) changing the macros in his .tex files to his newer macros
  a) ex: \myinput{} is changed to \newpage\input{}
  b) \section{} is changed to \sectionthree{}
  c) \begin{python0} , \input{solutions.tex}, and the accompanying macros/code to set up solutions that Liow uses
 2) putting python code in a seperate individual file, then writing it to a .tex file that will be inputted in the main compiled .tex code
 3) putting questions and answers in a seperate "exercises" directory, so it hyperlinks in the pdf. (done through Liow's solutions.py code)

# check documentation on fedora-installation's README.txt file to update your fedora VM

# To set up links through Liow's pdfs to create solutions ...
first go into superuser mode

type in: ln -s /usr/lib/python3.7/site-packages/solutions.py /usr/local/bin/solutions

now the command 'solutions' will work when wanting to link an exercise with it's solutions in Latex.

for example, in directory notes, make a directory named exercises, go into this directory and execute 'solutions make-ex example-0'

cut the exercise from the tex file in the notes directory, and paste it into exercises/example-0/question.tex

this will create a directory for example-0, now in the tex file of where this exercise is, do input{exercises/example-0/main.tex} so a link will be created
