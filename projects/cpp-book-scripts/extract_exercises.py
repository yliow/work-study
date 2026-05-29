'''
extracts exercises from a main.tex file for a given chapter, creates an "exercises" folder if one does not exist.

a given exercises will take the form of "num-of-exercise_chapter.tex", and will be inserted at the line the program found an instance of \begin{ex}, while stripping out the entire exercise block

the file layout should be

../notes/
  |
  +-- chapters/ <- all our chapters are in here
      |
      +-- exercises/ <- all our exercises are in here, each under their own "chapname/chapname_ex_1/" folder

'''

import os

'''
ex_dest = file location string
note = specific chapter string
ex_content = ordered list of strings representing the exercise
number = int ID of exercise
'''

def extraction_to_file(ex_dest, note, ex_content, number):
  #formatting for file/console printout, should just be 'num-chapter' 
  note = note.replace('/main.tex', '')
  
  #'solutions' works off the local dir so we change to that dir, we change back on return
  os.chdir(ex_dest)

  #assign file name and string for question.tex
  ex_file = str(number) + '-' + note
  question = ex_file + '/question.tex'
  
  #call solutions for this exercise
  os.system("solutions make-ex %s" % ex_file)
  
  try:
    with open(question, 'w') as x:
      x.write("\\tinysidebar{\\debug{exercises/{test/question.tex}}}\n")
      for entry in ex_content:
        x.write(entry)
  except Exception as e:
    print("!!!!!!! ERROR WRITING EXERCISE %s TO FILE, MESSAGE = %s" % (question, e))
    ex_file = None
  return ex_file

#constants
begin = r'\begin{ex}'
end = r'\end{ex}'

#directory access
dir_ = os.getcwd()

chapters = dir_ + '/chapters/'

chap_list = os.listdir(chapters)

write_dir = dir_ + '/temp/'

if not os.path.exists(write_dir):
  print("making temp dir\n")
  os.system("mkdir %s" % write_dir)
  
for chap in chap_list:
  note = chapters + chap + '/main.tex'
  exercises= []

  ex_acc = []
  note_acc = []
  ex_dest = dir_ + '/temp/' + chap + '/exercises/'
  
  try:
    #check if note dir exists
    if not os.path.exists(dir_ + '/temp/' + chap + '/'):
      print("making chapter %s dir..." % chap)
      os.system("mkdir %s" % (dir_ + '/temp/' + chap + '/'))
      
    #check if exercise dir exists
    if not os.path.exists(ex_dest):
      os.system("mkdir %s" % ex_dest)
      print("making exercise folder for chapter", chap)
      
    with open(note, 'r') as n:
      counter = 0
      flag = False
      n = n.readlines()
      
      for line in n:

        if begin in line:
          flag = True
          ex_acc.append(line)
          
        elif end in line:
          flag = False
          ex_acc.append(line)
          
          #call exercise maker
          exercise = extraction_to_file(ex_dest, note.replace(chapters, ''), ex_acc, counter)
          ex_acc = []
          counter += 1
          
          if exercise != None:
            note_acc.append(r"\input{../exercises/%s/question.tex}" % exercise )
          else:
            raise Exception("MALFORMED EXERCISE, COULD NOT CREATE")
          
        elif flag:
          ex_acc.append(line)
          
        else:
          note_acc.append(line)
      
    old_main = chapters + chap + '/old_main.tex'
    os.system("mv %s %s" % (note, old_main))
      
    #write new file
    with open(note, 'w') as f:
      for line in note_acc:
        f.write(line)
        
  #remove chapter on failure? dont want to include half-baked chaps
  except Exception as e:
    print("ERROR: could not extract exercises from chapter %s, message: %s" % (chap, e))
