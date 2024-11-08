import os
import shutil
import config as con

def get_num():
    num = 1
    for i in con.contents:
        for j in range(1, len(i[1])):
            if i[1][j].isdigit() and i[1][j - 1] == 'q':
                t = int(i[1][j:j + 2])
                if (t > num):
                    num = t
    return num

def file_struct():
    if os.path.exists(con.newpath + con.assignment):
        shutil.rmtree(con.newpath + con.assignment)
    num = get_num()
    for i in range(1, num + 1):
        s = rf"{con.newpath}{con.assignment}/{con.assignment}q{i:0>2}/doc/"
        os.makedirs(s + 'src')
        os.makedirs(s + 'skel')
