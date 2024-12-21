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
assignment = "a01"
assignment_it = "1";
basepath = "New/" # insert path for new directory (you are able to go back)
destination = basepath + assignment
# basepath = 
# go to basepath, write, then go back to cwd

# nln or sln is to determine whether to put a new page at the begining or
# or a solution

#latex
# contents[i][0] is the type of documents we are copying
# - QUEST_CODE is a coding question
# - QUEST_MATH is a math question that needs a lates answer file
# - SKELETON is the skelenton code that will be called by one of the files
# - SKEL_PDF is the skelenton code that will not be called by one of the
#   files but included on the pdf
# - OTHER is any other latex files that needs to be included
# - DOCUMENTS is any file that need to be in the pdf and is particular
#   to an assignment question and is included in the pdf
# - EXTRA_DOCUMENTS is same as DOCUMENTS but it appearance in the pdf
#   depends on assignment question

contents = [(at.OTHER, "Old/objectives.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.OTHER, "Old/instructions.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "Old/q01.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "Old/q02.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "Old/q03.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "Old/q04.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "Old/q05.tex"),
            (at.LATEXSTR, r"\newpage")
            ]
###########################################################################
