import os
'''
current ideas for fixing functions or processes
reconfigure the "line" variable in the EXERCISE class to just read the file the
function is writing to, make an exercise and link it right then and there instead
of actually saving it as a variable
'''
#CONSTANTS FOR COURSES
course_prefix = ['240', '245', '350', '358', '360', '362', '370', '380', '430', '451']

#this is just for testing purposes at the moment, will be changed later
working_course_prefix = 'cpp'

print('current exercise naming prefix:', working_course_prefix) 

'''
this matches the working course directory with the intended prefix for exercises
'''
#move this all into a function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# for i in course_prefix:
    # if x == None:
    #     print('lololololol')
course_exercise_name = ['cpp', 'adv', 'algo', 'alg2', 'asmb', 'auto', 'osym','gfx', 'data', 'cryp']

'''
copies the contents as a string, runs "solutions make-ex" to create an exercise sequentially as it goes down the file
>>>HOW TO USE<<<
'''

'''
this function will also paste the exercise name into the notes, immediately
linking it within the chapter for instant compilation tests
>>>HOW TO USE<<<
'''
def link_exercise_in_chapter():
    return

'''
the point of this class is to collect all the current exercises in this scanned
chapter, categorize them according to their place in the notes and then
associate a solution with them if they have one or are supposed to have one
exercises that do not are simply activities and their "answer.tex" file deleted
title, chapter, course and has_solution are self-explanatory, line is the line
the exercise was found at relative to the offset of the question before the exercise
>>>HOW TO USE<<<
'''
class EXERCISE:
    def __init__(self, TITLE, CHAPTER, COURSE, HAS_SOLUTION, LINE):
        self.TITLE = TITLE
        self.CHAPTER = CHAPTER
        self.COURSE = COURSE
        self.HAS_SOLUTION = False
        self.LINE = -1
'''
this function will look at every exercise that does not have the unified
naming scheme, rename all that do not comply up and change relevant exercise text
of the subsequent .tex files inside
>>>HOW TO USE<<<
pass a string in for working_course_prefix to change the exercise prefix
'''
def change_ex_dir_name(working_course_prefix):
    course_iterator = 1
    for directory, b, c in os.walk("."):
        #the "+2" is to cut off the "./" that would interfere with prefix matching
        print('looking at', directory)
        print('working prefix =', working_course_prefix)
        
        #slight issue here, its looking at the directory its being called in and
        #is saying that *that* directory is an invalid name, despite not having
        #a name and returns an empty string. working on a fix
        if (directory[2:len(working_course_prefix) + 2] != working_course_prefix) and directory != '.':
            print(directory[2:len(working_course_prefix) + 2], 'does not match', working_course_prefix, 'renaming and moving...')
            new_dir_name = working_course_prefix + '-' + str(course_iterator)
            print('new directory name =', new_dir_name)
            move_exercise_arg = 'mv ' + directory[2:] + ' ' + new_dir_name
            print('debug, running', move_exercise_arg)
            os.system(move_exercise_arg)
            
            #change_ex_content_names(new_dir_name)
        course_iterator += 1

def change_ex_content_names(dir_name):
    print("changing file contents of", dir_name)
    os.chdir(dir_name)
    answer_tex = open('answer.tex')
    question_tex = open('question.tex')
    main_tex = open('main.tex')
    print(answer_tex[:10])
    return
    
'''
finds an exercise, beginning with begin{ex} and ending with end{ex}
>>>HOW TO USE<<<
'''
def find_ex():
    return

'''
if the program finds a solution for the exercise, it will mark it as an
exercise. if not, it will mark it as an activity. this is prone to errors so
there will be a method of conclusively deciding what is an exercise and what is
simply an activity before being fully implemented
>>>HOW TO USE<<<
'''

'''
this function will maintain the original notes structure, copying the contents to
a new main.tex along with the exercises found at the correct line
>>>HOW TO USE<<<
'''
def copy_chapter_chunk():
    return
change_ex_dir_name('cpp')
