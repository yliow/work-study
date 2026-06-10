'''
moves requisite files to compile individual chapters
should be executed AFTER extract_exercises.py and split_chapters.py
'''

import os

#constants
thismac = 'thismacros.tex'
thispre = 'thispreamble.tex'
thispost = 'thispostamble.tex'
thispack = 'thispackages.tex'
thistitle = 'thistitle.tex'
make = 'makefile'
#already installed on vm, not needed
# latexcirc = 'latexcircuit.py'
# latextool = 'latextool_basic.py'

compilation_files = [thismac, thispre, thispost, thispack, thistitle, make]

#dirs
dir_ = os.getcwd()

#set to cpp-book dir
dir_ = dir_[:dir_.rfind('projects')] + 'courses/cpp-book/notes'

chapdir = dir_ + '/temp/'

f = os.listdir(chapdir)

for chaps in f:
  #check if necessary files exist under dir
  bookdir = chapdir + '/' + chaps + '/'
  
  #copy necessary files to book directory
  for file_ in compilation_files:
    os.system('cp %s %s' % (dir_ + '/' + file_, bookdir))

  #move existing chap file
  os.system("mv %s %s" % (chapdir + chaps + '/chap.tex', chapdir + chaps + '/book/chap.tex'))
  #create a proper "main.tex" for the chapter
  with open(bookdir + 'main.tex', 'w') as mtex:
    mtex.write(r'\input{thispreamble.tex}' + '\n')
    mtex.write(r'\clearsolutions' + '\n')
    mtex.write(r'\input{chap.tex}' + '\n')    
    mtex.write(r'\input{thispostamble.tex}' + '\n')

  #update thistitle.tex
  with open(bookdir + 'thistitle.tex', 'w') as title:
    title.write("\\renewcommand\\TITLE{%s}" % chaps)
    title.write(r"""
    \renewcommand\AUTHOR{\SHORTAUTHOR}
    \renewcommand\EMAIL{}
    """)

