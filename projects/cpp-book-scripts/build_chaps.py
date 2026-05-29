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
latexcirc = 'latexcircuit.py'
latextool = 'latextool_basic.py'
make = 'makefile'
compilation_files = [thismac, thispre, thispost, thispack, thistitle, latexcirc, latextool, make]


#dirs
dir_ = os.getcwd()
chapdir = dir_ + '/temp/'

f = os.listdir(chapdir)

for chaps in f:
  #check if necessary files exist under dir
  bookdir = chapdir + '/' + chaps + '/book/'
  if not os.path.exists(bookdir):
    os.system('mkdir %s' % bookdir)

  #copy necessary files to book directory
  for file_ in compilation_files:
    os.system('cp %s %s' % (dir_ + '/' + file_, bookdir))
