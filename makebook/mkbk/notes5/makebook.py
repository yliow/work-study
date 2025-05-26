import os
#from ekap import *
from chkbook import *

new_dir = os.getcwd() + 'newbook/'
#this program will copy the contents of the file and move them into a new folder that is distinct from the original file, organize the copy and try to run 'make'

#make a new directory
def make_new_book_dir():
    os.system('mkdir newbook')
    os.chdir(new_dir)
    check()
    return

#looks at all the .tex files within the directory and moves the files not explicity in the blacklist into the chapters folder
def movechaps(f):
    blacklist = ['thispreamble', 'thispostamble', 'thismacros', 'main']
    for i in blacklist:
        if f.find(i) >= 0:
            print('%s, not copying' % f)
            return
        else:
            os.system('cp %s %s' % (f, new_dir + f))
            return

#moves all the stdout into the correct stdout folder
def movestd(f):
    os.system('cp %s %s' % (f, new_dir + i))
    return

def sort_and_move():
    f = os.listdir()
    for i in f:
        print('looking at %s' % i)
        if i.find('.tex') >= 0:
            movechaps(i)
            print('moving %s ...' % i)
        elif i.find('stdout') >= 0:
            movestd(i)
            print('moving %s ...' % i)
        else:
            print('not moving %s' % i)
