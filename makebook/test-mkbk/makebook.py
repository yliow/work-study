import os
#from ekap import *
from chkbook import *

#for important messages
def dbg_txt(msg):
    for i in range(len(msg) + 4):
        print('=', end='')
    print()
    print("| %s |" % msg)
    for i in range(len(msg) + 4):
        print('=', end='')
    print()
    
old_dir = os.getcwd() + '/'    
new_dir = os.getcwd() + '/newbook/'

#this program will copy the contents of the file and move them into a new folder that is distinct from the original file, organize the copy and try to run 'make'

#make a new directory
def make_new_book_dir():
    try:
        print("enter a name for the new directory of notes:")
        name = input()
        os.system('mkdir %s' % name)
        print("created new directory for compiled book at", new_dir)
        os.chdir(new_dir)
    except Exception as e:
        dbg_text("ERROR: " + str(e))
        dbg_txt("REMAKING DIRECTORY")
        os.system('rm newbook -r')
        os.system('mkdir newbook')
        print("created new directory for compiled book at", new_dir)
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
            os.system('cp %s %s' % (old_dir + f, new_dir + 'chapters/' + f))
            return

#moves all the stdout into the correct stdout folder
def movestd(f):
    os.system('cp %s %s' % (old_dir + f, new_dir + 'stdout/' + f))
    return

#moves files that are to be in the same level dir as makebook and the chaps
def moveother(f):
    os.system('cp %s %s' % (old_dir + f, new_dir + f))
    
def make_book(new_dir_name='newbook'):
    f = os.listdir()
    make_new_book_dir()
    for i in f:
        print('looking at %s' % i)
        # if '.tex' in i:
        #     moveother(i)
        #     print('TEX FILE: moving %s ...' % i)
        if 'stdout' in i:
            movestd(i)
            print('STDOUT FILE: moving %s ...' % i)
        else:
            print('AUXILLARY FILE: %s' % i)
            moveother(i)
