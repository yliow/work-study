###########################################################################
#              THIS IS A TEMPLATE FOR THE "config.py" file!!
#              LOOK AT PDF TO DETERMINE THE STRUCTURE OF "config.py"
###########################################################################

# depends on file structure
name = "yliow"
courses = "ciss358"

FIRST_FILE_STRUCTURE = False # do the initial file structure, false if we want to do the other one
newpath = "test/ciss358/" # insert path for new directory (you are able to go back)
assignment = "a02"
# basepath = 
# go to basepath, write, then go back to cwd

# nln or sln is to determine whether to put a new page at the begining or
# or a solution

OTHER = 'other'
LATEXSTR = 'latex string'
QUEST_CODE = 'QUESTION'
QUEST_MATH = 'question'

#latex
# contents[i][0] is the type of documents we are copying
# - QUESTION is a coding question
# - question is a math question that needs a lates answer file
# - skel is the skelenton code that needs to be in the 
# - other is any other latex files that needs to be included
# - name of file
contents = [(OTHER, "../../courses/ciss358/a/a02/objective.tex"),
            (LATEXSTR, r"\newpage"),
            (OTHER, "../../courses/ciss358/a/a02/induction.tex"),
            (LATEXSTR, r"\newpage"),
            (QUEST_MATH, "../../courses/ciss358/a/a02/q01.tex"),
            (LATEXSTR, r"\newpage"),
            (OTHER, "../../courses/ciss358/a/a02/primes.tex"),
            (LATEXSTR, r"\newpage"),
            (QUEST_MATH, "../../courses/ciss358/a/a02/q02.tex"),
            (LATEXSTR, r"\newpage"),
            (QUEST_MATH, "../../courses/ciss358/a/a02/q03.tex")]
###########################################################################
