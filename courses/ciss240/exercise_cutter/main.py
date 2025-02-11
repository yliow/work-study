import os
#CONSTANTS FOR COURSES
course_iterator = 0
course_prefix = ['240', '245', '350', '358', '360', '362', '370', '380', '430', '451']
working_course_prefix = 'cpp'
working_naming_scheme = working_course_prefix + '-'

#this matches the working course directory with the intended prefix for exercises
#move this all into a function!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in course_prefix:
    if x == None:
        print('lololololol')
course_exercise_name = ['cpp', 'adv', 'algo', 'alg2', 'asmb', 'auto', 'osym','gfx', 'data', 'cryp']
#finds an exercise, beginning with "\begin{ex}" and ending with "\end{ex}"

#copies the contents as a string, runs "solutions make-ex" to create an exercise
#sequentially as it goes down the file

#if the program finds a solution for the exercise, it will mark it as an
#exercise. if not, it will mark it as an activity. this is prone to errors so
#there will be a method of conclusively deciding what is an exercise and what is
#simply an activity before being fully implemented

#this program will also paste the exercise name into the notes, immediately
#linking it within the chapter for instant compilation tests
def link_exercise_in_chapter():
    return

#this program will look at every exercise that does not have the unified
#naming scheme, rename it according to "the highest counted exercise suffix + 1"
#and change sidebar text of the subsequent .tex files inside
class EXERCISE:
    def __init__(self, TITLE, CHAPTER, COURSE):
        self.TITLE = TITLE
        self.CHAPTER = CHAPTER
        self.COURSE = COURSE

#print(os.getcwd())
for a, b, c in os.walk("."):
    print(os.getcwd())
    if a[:len(working_course_prefix)] != working_course_prefix:
        os.rename(a, working_course_prefix + '-'
                  + "{%01d}" + str(course_iterator))
    print("----")
    print("a: %s\n" % a)
    print("b: %s\n" % b)
    print("c: %s\n" % c)
    course_iterator += 1
def find_exercise():    
    return
