#get rid of changes after running extract_exercise.py
import os

dir_ = os.getcwd() + '/chapters'
chapters = os.listdir(dir_)

for i in chapters:
  try:
    new_main = dir_ + '/' + i + '/new_main.tex'
    old_main = dir_ + '/' + i + '/old_main.tex'
    os.system('rm %s' % new_main)
    os.system('rm %s' % old_main)
  except Exception as e:
    print("ERROR, CANT REMOVE FILE %s, MESSAGE %s" % (dir_ + '/' + i, e))
