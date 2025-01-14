import os
import config as con
import shutil

struct = {}


def file_struct1(path, num):
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
        
        struct['q doc%(i)s'%{'i': str(i)}] = s + 'question/doc'#CLEANUP
        struct['a doc%(i)s'%{'i': str(i)}] = s + 'answer/doc'
        struct['q src%(i)s'%{'i': str(i)}] = s + 'question/src'
        struct['a src%(i)s'%{'i': str(i)}] = s + 'answer/src'
        struct['skel%(i)s'%{'i': str(i)}] = s + 'question/skel'

File_type = [file_struct1, file_struct2]

VERS = 0
FILE_VERSION = File_type[VERS] # do the initial file structure, false if we wantOTHER = 'other'

OTHER = "other document"
EXTRA_DOCUMENTS = "extra_documents"
DOCUMENTS = "documents"
LATEXSTR = 'latex string'
QUEST_CODE = 'QUESTION'
QUEST_MATH = 'question'
SKELETON = 'skeleton'
SKEL_PDF = 'skel in pdf'


def writefile(path, s):
    f = open(os.path.join(con.destination, path), "w")
    f.write(s)
    f.close()

def is_latex(path):
    return path.endswith('.tex')

def is_answer(path):
    path = os.path.split(path)[-1]
    return path.endswith('s.tex') and path[0] == 'q'

def include_latex(path):
    '''
    returns one of the following with ... replaced by path
    \myinludetex{...}
    \input{...}
    \subimport{...}
    '''
    if is_answer(path):
        return r'''\myincludetex{%s}''' % path
    else:
        dir_, file_ = os.path.split(path)
        if dir_ == "":
            return r'''\input{%s}''' % path
        else:
            return r'''\subimport*{%s}{%s}''' % os.path.split(path)
    return ""

def include_src(path, frame='single', fontsize='\\footnotesize'):
    #src = r'''\VerbatimInput[frame=%(frame)s,font=%(fontsize)s]{%(path)s}
    #''' % {'path':path, 'frame':frame, 'fontsize':fontsize}
    src = r"\myincludesrc{%s}" % path
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

def file_getter(path):#DELETE
    end = len(path)
    start = end - 1
    
    while start != 0:
        if path[start] == '/':
            return path[start + 1: end]
        start -= 1
    return path[start: end]


def copy_path(oldpath, newpath):#CLEANUP: DELETE
    shutil.copy(oldpath, newpath)

QUESTION_ITERATOR = 0
    
def include(path):
    s = ''
    # what assignment question number we are on
    global QUESTION_ITERATOR

    # DOCUMENT TYPES
    global OTHER
    global LATEXSTR
    global QUEST_CODE
    global QUEST_MATH
    global SKELETON
    global SKEL_PDF
    global EXTRA_DOCUMENTS
    global DOCUMENTS
    
    i = QUESTION_ITERATOR
    
    if path[0] == QUEST_CODE or path[0] == QUEST_MATH:
        
        i += 1
        dest = struct['q doc%(i)s'%{'i': str(i)}]#CLEANUP
        question = '/q%s.tex' % str(i).zfill(2) 
        copy_path(path[1], dest + question)#CLEANUP: OS.PATH.JOIN()
        
        os.system("chmod a=r %s.tex" % (dest + question) )#CLEANUP: OS.PATH.JOIN()
        textpath = dest[len(con.destination) + 1:] + question
        
        s += '''Q%(question)s. %(textpath)s
''' %{'textpath':include_(textpath + '.tex'), 'question': i}
        
        if path[0] == QUEST_MATH:
            writefile(textpath + 's.tex', '')#CLEANUP: OS.PATH.JOIN()
            s += r'''\SOLUTION
%(textpath)s
''' %{'textpath': include_(textpath + 's.tex')}
    elif path[0] == EXTRA_DOCUMENTS or path[0] == DOCUMENTS:
        dest = struct['q doc%(i)s'%{'i': str(i)}]
        
        file_ = file_getter(path[1])
        copy_path(path[1], dest + '/' + file_)
        if path[0] == DOCUMENTS:
            textpath = dest[len(con.destination) + 1:] + '/' + file_
            
            s += ''' %(textpath)s
''' %{'textpath':include_(textpath)}

    elif path[0] == LATEXSTR:
        s = path[1] + ' '
      
    elif path[0] == SKELETON or path[0] == SKEL_PDF:
        file_ = file_getter(path[1])
        dest = struct['skel%(i)s'%{'i': str(i)}]#CLEANUP
        copy_path(path[1], dest + '/' + file_) #CLEANUP: OS.PATH.JOIN()
        textpath = dest[len(con.destination) + 1:] + '/' + file_#CLEANUP: OS.PATH.JOIN()
        if path[0] == SKEL_PDF:
            s += '''%(textpath)s
'''%{'textpath': include_(textpath)}
        
    elif path[0] == OTHER:
        file_ = file_getter(path[1])
        dest = con.destination
        copy_path(path[1], dest + '/' + file_)#CLEANUP: OS.PATH.JOIN()
        s += '''%(textpath)s
'''%{'textpath': include_(file_)}
    QUESTION_ITERATOR = i
    return s
