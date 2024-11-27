import attributes as at
###########################################################################
#              THIS IS A TEMPLATE FOR THE "config.py" file!!
#              LOOK AT PDF TO DETERMINE THE STRUCTURE OF "config.py"
###########################################################################

#################################
#rename config to reflect assignment that has been generated using run.py
##################################################################
# depends on file structure
courses = "ciss240"
name = "yliow"
assignment = "a03"
assignment_it = "3";
basepath = "test/ciss240/" # insert path for new directory (you are able to go back)
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
contents = [(at.OTHER, "../../courses/ciss240/a/a03/objective.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "../../courses/ciss240/a/a03/a03q01/question/main.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "../../courses/ciss240/a/a03/a03q02/question/main.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "../../courses/ciss240/a/a03/a03q03/question/main.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "../../courses/ciss240/a/a03/a03q04/question/main.tex"),
            (at.LATEXSTR, r"\newpage")
            ]
###########################################################################
