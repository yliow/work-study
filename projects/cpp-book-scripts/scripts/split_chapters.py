'''
- makes a chap.tex for the current chapter (name pending)
- splits chapters by their section <- will have to update this as time goes on from current naming scheme
- writes found sections to "chap.tex" for its respective chapter
'''
import os

#constants
solution_header = r'''\begin{python0}
from solutions import *; clear()
\end{python0}
'''
footer_chaptex = r'''\begin{python0}
from solutions import *
prepare_solutions()
\end{python0}
\begin{python}
import os
os.system('cp solutions.tex solution.tex.backup')  
\end{python}
\input{solutions.tex}
\begin{python0}
from solutions import *
clear()
\end{python0}
'''
#directory access
dir_ = os.getcwd()

#set working notes dir
dir_ = dir_[:dir_.rfind('projects')] + 'courses/cpp-book/notes'

chapters = dir_ + '/temp/'

chap_list = os.listdir(chapters)

for chap in chap_list:
  note = chapters + chap + '/main.tex'
  sections = []

  #scan note to split into sections
  try:  
    with open(note, 'r') as f:
      file_ = f.readlines()
      content = []
    
      for line in file_:
        if r'\newpage\EMPHASIZE' in line:
          #check against empty content list to prevent blank first section 
          if len(content) and (r'\newpage\EMPHASIZE' in line or r'\sectionthree' in line):
            sections.append(content)
            content = []
            content.append(line.replace(r'\newpage\EMPHASIZE', r'\sectionthree'))
          else:
            content.append(line.replace(r'\newpage\EMPHASIZE', r'\sectionthree'))
        else:
          content.append(line)
          
    print("CHAPTER %s SECTIONS LENGTH = " % chap, len(sections))
    
    #section iterator
    k = 0
    
    #sections collector for insertion into chap.tex file
    sections_list = []
    
    #write sections to file in chapter folder
    for s in sections:
      chap_section = str(k) + '-' + chap + '.tex'

      #open section
      with open(dir_ + '/temp/' + chap + '/' + chap_section, 'w') as t:

        #write solution header
        t.write(solution_header)
        
        #add to section list for writing to chap.tex later
        sections_list.append(chap_section)

        #write section
        for line in s:
          t.write(line)
          
      k += 1
      
      #write sections to chap.tex file
      with open(dir_ + '/temp/' + chap + '/chap.tex', 'w') as chaptex:
        for entry in sections_list:
          chaptex.write("\\input{%s}\n" % entry)
        
        #write footer for chap.tex
        chaptex.write(footer_chaptex)
        if os.path.exists(dir_ + '/temp/' + chap + '/main.tex'):
          print("removing old main.tex...")
          os.system("rm %s" % (dir_ + '/temp/' + chap + '/main.tex'))
  except Exception as e:        
    print("FAILURE PARSING NOTE %s, MESSAGE = %s" % (note, e))
