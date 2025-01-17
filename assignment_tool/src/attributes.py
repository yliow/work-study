import os
import config as con
import shutil

struct = {}

VERS = 0

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
        dest = struct['q doc%s'% str(i)]#CLEANUP
        question = 'q%s.tex' % str(i).zfill(2) 
        #copy_path(path[1], dest + question)#CLEANUP: OS.PATH.JOIN()
        shutil.copy(path[1], os.path.join(dest, question))
        os.system("chmod a=r %s" % os.path.join(dest, question) )#CLEANUP: OS.PATH.JOIN()
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
        dest = struct['skel%s'% str(i)]#CLEANUP
        copy_path(path[1], os.path.join(dest, file_)) #CLEANUP: OS.PATH.JOIN()
        textpath = os.path.join(dest[len(con.destination) + 1:], file_)#CLEANUP: OS.PATH.JOIN()
        if path[0] == SKEL_PDF:
            s += '''%(textpath)s
'''%{'textpath': include_(textpath)}
        
    elif path[0] == OTHER:
        file_ = os.path.split(path[1])[-1]
        dest = con.destination
        copy_path(path[1], os.path.join(dest, file_))#CLEANUP: OS.PATH.JOIN()
        s += '''%(textpath)s
'''%{'textpath': include_(file_)}
    QUESTION_ITERATOR = i
    return s
