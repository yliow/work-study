'''
extracts exercises from a main.tex file for a given chapter, creates an "exercises" folder if one does not exist.

a given exercises will take the form of "num-of-exercise_chapter.tex", and will be inserted at the line the program found an instance of \begin{ex}, while stripping out the entire exercise block

the file layout should be

../notes/
  |
  +-- chapters/ <- all our chapters are in here
  |
  +-- exercises/ <- all our exercises are in here, each under their own "chapname/chapname_ex_1/" folder
  |
  ...

'''

import os

#extracts an exercise, uses the file name immediately above the main.tex file its looking at as the exercise name, formatted as "print_strings_1.tex"
def extract(file_):
  
  return

dir_ = os.getcwd()
chap_dir = dir_ + '/chapters/'
ex_folder = dir_ + '/exercises/'

notes_files = os.listdir(chap_dir)

for chapter in notes_files:
  print(chap_dir + chapter)

print(ex_folder)

if not os.path.exists(ex_folder):
  print("CREATING EXERCISE FOLDER AT %s" % ex_folder)
  os.system("mkdir %s" % ex_folder)
  


#check for exercise folders first
for chapter in notes_files:
  note = chap_dir + chapter
  note_exercises = ex_folder + chapter + '/'
  
  
#extract exercises
for chapter in notes_files:
  

    
