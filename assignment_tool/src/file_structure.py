import os
import shutil
import config as con
import attributes as at

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
    at.FILE_VERSION(path, num) # change to at.mk_directories
    return True
