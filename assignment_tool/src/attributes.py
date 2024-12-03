import os
import config as con
import shutil

struct = {}


def file_struct1(path, num):
    for i in range(1, num + 1):
        s = rf"{path}q{i:0>2}/"
        stru = s + 'doc'
        os.makedirs(stru)
        struct['q doc%(i)s'%{'i': str(i)}] = stru
        struct['a doc%(i)s'%{'i': str(i)}] = stru
        os.makedirs(s + 'src')
        struct['q src%(i)s'%{'i': str(i)}] = s + 'src'
        struct['a src%(i)s'%{'i': str(i)}] = s + 'src'
        os.makedirs(s + 'skel')
        struct['skel%(i)s'%{'i': str(i)}] = s + 'skel'
        
def file_struct2(path, num):
    for i in range(1, num + 1):
        s = rf"{path}q{i:0>2}/"
        os.makedirs(s + 'question')
        os.makedirs(s + 'answer')
        os.makedirs(s + 'question' + '/doc')
        os.makedirs(s + 'question' + '/src')
        os.makedirs(s + 'question' + '/skel')
        os.makedirs(s + 'answer' + '/doc')
        os.makedirs(s + 'answer' + '/src')
        
        struct['q doc%(i)s'%{'i': str(i)}] = s + 'question/doc'
        struct['a doc%(i)s'%{'i': str(i)}] = s + 'answer/doc'
        struct['q src%(i)s'%{'i': str(i)}] = s + 'question/src'
        struct['a src%(i)s'%{'i': str(i)}] = s + 'answer/src'
        struct['skel%(i)s'%{'i': str(i)}] = s + 'question/skel'

File_type = [file_struct1, file_struct2]

VERS = 0
FILE_VERSION = File_type[VERS] # do the initial file structure, false if we want to do the other one



#rename "newpath" to a more descriptive name, target, dest, base etc.




#store these constants in a different file
OTHER = 'other'
EXTRA_DOCUMENTS = "documents"
LATEXSTR = 'latex string'
QUEST_CODE = 'QUESTION'
QUEST_MATH = 'question'
SKELETON = 'skeleton'


def writefile(path, s):
    f = open(con.destination + '/' + path, "w")
    f.write(s)
    f.close()

def is_latex(path):
    x = path[len(path) - 4:]
    return x == '.tex'

def is_answer(path):
    x = path[len(path) - 5:]
    return x == 's.tex'

def include_latex(path):
    if (is_answer(path)):
        return r'''\myincludetex{%(path)s}''' %{'path':path}
    #else:
    #    return r'''\input{%(path)s}''' %{'path':path}
    else:
        file_ = file_getter(path)
        len_ = len(path) - len(file_)
        directory = path[:len_]
        print(directory)
        return r'''\subimport*{%(path)s}{%(file)s}''' %{'path': directory, 'file': file_}
    
    return ""

def include_src(path, frame='single', fontsize='\\footnotesize'):
    #src = r'''\VerbatimInput[frame=%(frame)s,font=%(fontsize)s]{%(path)s}
    #''' % {'path':path, 'frame':frame, 'fontsize':fontsize}
    src = r"\myincludesrc{%(path)s}" % {'path':path}
    return src

def include_(path):
    if is_latex(path):
        return include_latex(path)
    else:
        return include_src(path)

def solution(path):
    if path == 'sln':
        return r'\SOLUTION'
    elif path == 'nln':
        return r'\newpage'
    return ''

def file_getter(path):
    end = len(path)
    start = end - 1
    
    while start != 0:
        if path[start] == '/':
            return path[start + 1: end]
        start -= 1
    return path[start + 1: end]


def copy_path(oldpath, newpath):
    shutil.copy(oldpath, newpath)

QUESTION_ITERATOR = 0
    
def include(path):
    s = ''
    global QUESTION_ITERATOR
    
    # global basepath
    # global assignment
    # global assignment_it
    # global destination
    
    global OTHER
    global LATEXSTR
    global QUEST_CODE
    global QUEST_MATH
    global SKELETON
    global EXTRA_DOCUMENTS
    
    i = QUESTION_ITERATOR
    
    if path[0] == QUEST_CODE or path[0] == QUEST_MATH:
        
        i += 1
        dest = struct['q doc%(i)s'%{'i': str(i)}]
        question = '/q' + str(i).zfill(2)
        copy_path(path[1], dest + question + '.tex')
        
        os.system("chmod a=r " + dest + question + '.tex')
        textpath = dest[len(con.destination) + 1:] + question
        
        s += '''
        Q%(question)s. %(textpath)s''' %{'textpath':include_(textpath + '.tex'), 'question': i}
        
        if path[0] == QUEST_MATH:
            writefile(textpath + 's.tex', '')
            s += r'''
            
            \SOLUTION
            
            %(textpath)s''' %{'textpath': include_(textpath + 's.tex')}
    elif path[0] == EXTRA_DOCUMENTS:
        dest = struct['q doc%(i)s'%{'i': str(i)}]
        
        file_ = file_getter(path[1])
        copy_path(path[1], dest + '/' + file_)
        
        
    elif path[0] == LATEXSTR:
        s = path[1]
    elif path[0] == SKELETON:
        file_ = file_getter(path[1])
        dest = struct['skel%(i)s'%{'i': str(i)}]
        copy_path(path[1], dest + '/' + file_)
        textpath = dest[len(con.destination) + 1:] + '/' + file_
        s += '''
        %(textpath)s'''%{'textpath': include_(textpath)}
        
    elif path[0] == OTHER:
        
        file_ = file_getter(path[1])
        dest = con.destination
        
        copy_path(path[1], dest + '/' + file_)
        
        s += '''
        %(textpath)s'''%{'textpath': include_(file_)}
    QUESTION_ITERATOR = i
    return s
