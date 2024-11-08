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
        shutil.rmtree(con.newpath + con.assignment)
    num = get_num()
    for i in range(1, num + 1):
        s = rf"{con.newpath}{con.assignment}/{con.assignment}q{i:0>2}/doc/"
        os.makedirs(s + 'src')
        os.makedirs(s + 'skel')
