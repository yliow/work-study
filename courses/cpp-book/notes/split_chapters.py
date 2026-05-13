'''
makes a chap.tex for the current chapter (name pending)
splits chapters by their
'''
import os

#constants
solution_header = r'''
\begin{python0}
from solutions import *; clear()
\end{python0}
'''


dir_ = os.getcwd()

chapters = dir_ + '/chapters/'

chap_list = os.listdir(chapters)

for chap in chap_list:
  note = chapters + chap + '/main.tex'

  sections = []

  #scan note to split into sections
  try:  
    with open(note, 'r') as f:
      file_ = f.readlines()
      flag = False
      content = []
    
      for line in file_:
    
        if r'\newpage\EMPHASIZE' in line:
          print("NEWPAGE FOUND!!!")
          #check against empty content list to prevent blank first section 
          if len(content) and r'\newpage\EMPHASIZE' in line:
            sections.append(content)
            content = []
            content.append(line.replace(r'\newpage\EMPHASIZE', r'\sectionthree'))
          else:
            content.append(line.replace(r'\newpage\EMPHASIZE', r'\sectionthree'))
        else:
          content.append(line)
          
    if not (os.path.exists(dir_ + '/temp')):
      os.system('mkdir temp')
    
    with open(dir_ + '/temp/' + chap + '.tex', 'w') as t:
      for s in sections:
        for line in s:
          t.write(line)
  except Exception as e:        
    print("FAILURE PARSING NOTE %s, MESSAGE = %s" % (note, e))
