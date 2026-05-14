#mk_directories.py
import os
import shutil
import config as con
import attributes as at


def mk_directories_1(path, num): # change to mk_directories_1
    for i in range(1, num + 1):
        s = rf"{path}q{i:0>2}/"
        stru = s + 'doc'
        os.makedirs(stru)
        at.struct['q doc%(i)s'%{'i': str(i)}] = stru#CLEANUP
        at.struct['a doc%(i)s'%{'i': str(i)}] = stru
        os.makedirs(s + 'src')
        at.struct['q src%(i)s'%{'i': str(i)}] = s + 'src'
        at.struct['a src%(i)s'%{'i': str(i)}] = s + 'src'
        os.makedirs(s + 'skel')
        at.struct['skel%(i)s'%{'i': str(i)}] = s + 'skel'
        
def mk_directories_2(path, num): # change to mk_directories_2
    for i in range(1, num + 1):
        s = rf"{path}q{i:0>2}/"
        os.makedirs(s + 'question')
        os.makedirs(s + 'answer')
        os.makedirs(s + 'question' + '/doc')
        os.makedirs(s + 'question' + '/src')
        os.makedirs(s + 'question' + '/skel')
        os.makedirs(s + 'answer' + '/doc')
        os.makedirs(s + 'answer' + '/src')
        
        at.struct['q doc%s'% str(i)] = s + 'question/doc'#CLEANUP
        at.struct['a doc%s'% str(i)] = s + 'answer/doc'
        at.struct['q src%s'% str(i)] = s + 'question/src'
        at.struct['a src%s'% str(i)] = s + 'answer/src'
        at.struct['skel%s'% str(i)] = s + 'question/skel'

File_type = [mk_directories_1, mk_directories_2] #cleanup

MK_DIR = File_type[at.VERS] # change to mk_directories
# do the initial file structure, false if we wantOTHER = 'other'

def get_num():
    num = 0
    for i in con.contents:
        if i[0] == 'question' or i[0] == 'QUESTION':
            num += 1
    return num

def file_struct(): #change name
    if os.path.exists(con.destination):
        print(con.destination)
        answer = input("^ this path already exist are you sure you want to overwrite it? enter [y/n]: ")
        if answer not in ["y", "yes", "yeah"]:
            return False
        else:
            shutil.rmtree(con.destination)
    num = get_num()
    path = rf"{con.destination}/{con.assignment}"
    MK_DIR(path, num) # change to at.mk_directories
    return True
