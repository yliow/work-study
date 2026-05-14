import os
import shutil

VERS = 0

def mk_directories_1(path, num): # change to mk_directories_1
    struct = {}
    for i in range(1, num + 1):
        s = rf"{path}q{i:0>2}/"
        stru = s + 'doc'
        os.makedirs(stru)
        struct['q doc%(i)s'%{'i': str(i)}] = stru#CLEANUP
        struct['a doc%(i)s'%{'i': str(i)}] = stru
        os.makedirs(s + 'src')
        struct['q src%(i)s'%{'i': str(i)}] = s + 'src'
        struct['a src%(i)s'%{'i': str(i)}] = s + 'src'
        os.makedirs(s + 'skel')
        struct['skel%(i)s'%{'i': str(i)}] = s + 'skel'

    return struct
        
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
        
        struct['q doc%s'% str(i)] = s + 'question/doc'#CLEANUP
        struct['a doc%s'% str(i)] = s + 'answer/doc'
        struct['q src%s'% str(i)] = s + 'question/src'
        struct['a src%s'% str(i)] = s + 'answer/src'
        struct['skel%s'% str(i)] = s + 'question/skel'
    return struct

File_type = [mk_directories_1, mk_directories_2] #cleanup

MK_DIR = File_type[VERS] # change to mk_directories
# do the initial file structure, false if we wantOTHER = 'other'

# def get_num():
#     num = 0
#     for i in question:
#         if i[0] == 'question' or i[0] == 'QUESTION':
#             num += 1
#     return num

# def file_struct(): #change name
#     if os.path.exists(a.destination):
#         print(a.destination)
#         answer = input("^ this path already exist are you sure you want to overwrite it? enter [y/n]: ")
#         if answer not in ["y", "yes", "yeah"]:
#             return False
#         else:
#             shutil.rmtree(a.destination)
#     num = get_num()
#     path = rf"{a.destination}/{a.assignment}"
#     MK_DIR(path, num) # change to at.mk_directories
#     return True
