import os
from file_structure import *
import latex_fragment as l
import makefile as m

def writefile(path, s):
    f = open(path, "w")
    f.write(s)
    f.close()


def include_latex(path, myincl):
    '''
    returns one of the following with ... replaced by path
    \myinludetex{...}
    \input{...}
    \subimport{...}
    '''
    if myincl:
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

def include_(path, myincl=False):
    if path.endswith(".tex"):
        return include_latex(path, myincl)
    else:
        return include_src(path)

class Assignment_Builder:
    def __init__(self, course, name,
                 assignment, basepath, num_assignment):
        self.course = course
        self.name = name
        self.assignment = assignment
        self.basepath = basepath
        self.destination = os.path.join(self.basepath, 'a%s' % str(self.assignment).zfill(2))
        self.content = []
        self.include_main_tex = ""
        self.question_iterator = 0
        self.num_assignment = num_assignment
        self.make()

    def add_files(self):
        for path, s in [l.add_maintex(self.include_main_tex),
                        l.thispreamble(self.assignment, self.course, self.name),
                        l.thispackages(), l.thispostamble(), l.thistitle(),
                        l.thismacros(),
                        m.makefile(self.num_assignment,
                                   'a%s' % str(self.assignment).zfill(2))]:
            writefile(os.path.join(self.destination, path), s)
                        
        
    def make(self):
        if os.path.exists(self.destination):
            print(self.destination)
            answer = input("^ this path already exist are you sure you want to overwrite it? enter [y/n]: ")
            if answer not in ["y", "yes", "yeah"]:
                return False
            else:
                shutil.rmtree(self.destination)
        num = self.num_assignment
        a = 'a%s' % str(self.assignment).zfill(2)
        path = rf"{self.destination}/{a}"
        self.struct = MK_DIR(path, num) # change to at.mk_directories
        return True
        
    def add_latexstr(self, s):
        self.include_main_tex += '\n' + s
    
    def add_programming_question(self, path):
        self.question_iterator += 1
        dest = self.struct['q doc%s'% str(self.question_iterator)]#CLEANUP
        question = 'q%s.tex' % str(self.question_iterator).zfill(2)
        #copy_path(path, dest + question)#CLEANUP: OS.PATH.JOIN()
        shutil.copy(path, os.path.join(dest, question))
        os.system("chmod a=r %s" % os.path.join(dest, question) )#CLEANUP: OS.PATH.JOIN()
        textpath = os.path.join(dest[len(self.destination) + 1:], question)
        
        self.include_main_tex += '''
Q%(question)s. %(textpath)s
''' %{'textpath':include_(textpath), 'question': self.question_iterator}

    # the add math question is 
    def add_math_question(self, path):
        self.add_programming_question(path)

        question = 'q%ss.tex' % str(self.question_iterator).zfill(2) 
        textpath = os.path.join(dest[len(self.destination) + 1:], question)
        writefile(textpath, '')#CLEANUP: OS.PATH.JOIN()
        self.include_main_tex += r'''
\SOLUTION
%(textpath)s
''' %{'textpath': include_(textpath + 's.tex', True)}
    def add_skeleton(self, path, in_pdf=True):
        file_ = os.path.split(path)[-1]
        print(file_)
        dest = self.struct['skel%s'% str(self.question_iterator)]#CLEANUP
        shutil.copy(path, os.path.join(dest, file_)) #CLEANUP: OS.PATH.JOIN()
        textpath = os.path.join(dest[len(self.destination) + 1:], file_)#CLEANUP: OS.PATH.JOIN()
        if in_pdf:
            self.include_main_tex += '''
%(textpath)s
'''%{'textpath': include_(textpath, True)}

    # so a quality i found in most extra documents is that they were either
    # referenced by another latex file or they were for a particular question
    # so the boolean in_pdf means are they gonna be referenced by the main.tex or not
    # and the boolean for question means are they gonna be used by a particular question
    # if they are they will be put in doc directory
    def add_extra_document(self, path, in_pdf=True, for_question=False):
        dest = ""
        if for_question:
            dest = self.struct['q doc%(i)s'%{'i': str(self.question_iterator)}]
        else:
            dest = self.destination
        
        file_ = os.path.split(path)[-1]
        print(file_)
        shutil.copy(path, os.path.join(dest, file_))
        if in_pdf:
            textpath = os.path.join(dest[len(self.destination) + 1:],file_)
            
            self.include_main_tex += '''
%(textpath)s
''' %{'textpath':include_(textpath)}
    

