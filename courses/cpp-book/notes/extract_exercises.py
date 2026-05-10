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

'''
ex_dest = file location string
note = specific chapter string
ex_content = ordered list of strings representing the exercise
number = int ID of exercise
'''

def extraction_to_file(ex_dest, note, ex_content, number):
  #formatting for file/console printout, should just be 'num-chapter' 
  note = note.replace('/main.tex', '')
  
  #directory for exercise and possible soln
  ex_console_name = ex_folder.replace(ex_dest, '')

  #'solutions' works off the local dir so we change to that dir, we change back on return to read_file
  # print("CHANGING TO: %s" % ex_dest)
  
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
    print("!!!!!!! ERROR WRITING EXERCISE %s TO FILE %s" % (question, e))
    ex_file = None
  return ex_file

#open and read file, then return a list of formatted exercises for that particular chapter
def read_file(note, ex_dest, chap_dir):
  #grabs lines that are part of an exercise block
  ex_accumulator = []
  new_note = []
  counter = 0
  flag = False
  
  with open(note, 'r') as f:
    f = f.readlines()
    for line in f:
      if ("\\begin{ex}") in line:
        flag = True
      elif "\\end{ex}" in line:
        flag = False        

        #get last line of ex
        ex_accumulator.append(line)
        #write to file, if its None then an error occurred writing so we abandon the chapter
        exercise_file_str = extraction_to_file(ex_dest, note.replace(chap_dir, ''), ex_accumulator, counter)
        
        #return to operating directory
        # print(">>>>CHANGING FROM: %s" % chap_dir.replace('/chapters/', ''))
        os.chdir(chap_dir.replace('/chapters', ''))
        #reset ex_accumulator
        ex_accumulator = []
        counter += 1
        
        if exercise_file_str != None:
          #process result
          new_note.append("\\input{%s}" % exercise_file_str)
        else:
          print("!!!!!! FAILED EXTRACTING EXERCISE IN CHAPTER %s, ABANDONING CHAPTER REWRITE !!!!!!!" % note)
          #needs to also clear the directory where it wrote all the exercises in this chapter (if there were any)
          return None
        
        continue
      
      if flag:
        ex_accumulator.append(line)
        
      #not in an exercise block, append line 
      else:
        new_note.append(line)
  return new_note, counter

#directory references
dir_ = os.getcwd()
chap_dir = dir_ + '/chapters/'
ex_folder = dir_ + '/exercises/'

#list of all notes under 'chapters'
notes_files = os.listdir(chap_dir)

if not os.path.exists(ex_folder):
  print("CREATING EXERCISE FOLDER AT %s" % ex_folder)
  os.system("mkdir %s" % ex_folder)
  
#check for exercise folders first
for chapter in notes_files:
  print("working on chapter: %s" % chapter)
  try:
    note = chap_dir + chapter + '/main.tex'

    # assign and write new note to file
    new_note, counter = read_file(note, ex_folder, chap_dir)
    new_note_location = chap_dir + chapter + '/new_main.tex'
    with open(new_note_location, 'w') as new_dest:
      for line in new_note:
        print("writing new_main.tex for chapter %s, extracted %s exercises to file\n" % (chapter, counter))
        new_dest.write(line)
  except Exception as e:
    print("!!!!!! ERROR PROCESSING CHAPTER: %s, MESSAGE: %s\n" % (chapter, e))
    
