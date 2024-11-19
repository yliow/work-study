import os
import shutil
import config as con

def get_num():
    num = 0
    for i in con.contents:
        if i[0] == 'question' or i[0] == 'QUESTION':
            num += 1

    return num

def file_struct():
    if os.path.exists(con.newpath + con.assignment):
        print(con.newpath + con.assignment)
        answer = input("^ this path already exist are you sure you want to overwrite it? enter [y/n] ")
        if answer == "y" or answer == "yes" or answer == "yeah":
            shutil.rmtree(con.newpath + con.assignment)
        else:
            return False
    
    num = get_num()
    if (con.FIRST_FILE_STRUCTURE):
        for i in range(1, num + 1):
            s = rf"{con.newpath}{con.assignment}/{con.assignment}q{i:0>2}/"
            os.makedirs(s + 'doc')
            os.makedirs(s + 'src')
            os.makedirs(s + 'skel')
    else:
        for i in range(1, num + 1):
            s = rf"{con.newpath}{con.assignment}/{con.assignment}q{i:0>2}/"
            os.makedirs(s + 'question')
            os.makedirs(s + 'answer')
            os.makedirs(s + 'question' + '/doc')
            os.makedirs(s + 'question' + '/src')
            os.makedirs(s + 'question' + '/skel')
            os.makedirs(s + 'answer' + '/doc')
            os.makedirs(s + 'answer' + '/src')
    return True
