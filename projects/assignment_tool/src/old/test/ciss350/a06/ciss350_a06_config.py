import attributes as at
###########################################################################
#              THIS IS A TEMPLATE FOR THE "config.py" file!!
#              LOOK AT PDF TO DETERMINE THE STRUCTURE OF "config.py"
###########################################################################

#################################
#rename config to reflect assignment that has been generated using run.py
##################################################################
# depends on file structure
courses = "ciss350"
name = "yliow"
assignment = "a06"
assignment_it = "1";
basepath = "test/ciss350/" # insert path for new directory (you are able to go back)
destination = basepath + assignment
# basepath = 
# go to basepath, write, then go back to cwd

# nln or sln is to determine whether to put a new page at the begining or
# or a solution

#latex
# contents[i][0] is the type of documents we are copying
# - QUESTION is a coding question
# - question is a math question that needs a lates answer file
# - skel is the skelenton code that needs to be in the 
# - other is any other latex files that needs to be included
# - name of file
contents = [(at.QUEST_CODE, "../../courses/ciss350/a/a06/questions/q00.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "../../courses/ciss350/a/a06/questions/q01.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "../../courses/ciss350/a/a06/questions/q02.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "../../courses/ciss350/a/a06/questions/q03.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "../../courses/ciss350/a/a06/questions/q04.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "../../courses/ciss350/a/a06/questions/q05.tex")
            ]
###########################################################################
