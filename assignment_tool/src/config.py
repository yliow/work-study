

###########################################################################
#              THIS IS A TEMPLATE FOR THE "config.py" file!!
#              LOOK AT PDF TO DETERMINE THE STRUCTURE OF "config.py"
###########################################################################

# depends on file structure
name = "yliow"
courses = "ciss240"

newpath = "test/" # insert path for new directory (you are able to go back)
assignment = "a06"

#TODO
# 1) fix formatting for question numbering
# 2) find a way to get the amount of questions
# 3) allow for backtracking through directories

# nln or sln is to determine whether to put a new page at the begining or
# or a solution

file_of_question = ['']
file_of_others = ['']

#latex
# contents[i][0] is the type of documents we are copying
# - QUESTION is a coding question
# - question is a math question that needs a lates answer file
# - other is any other latex files that needs to be included
# - name of file
contents = [("other", "../../courses/ciss240/a/a05/other/objective.tex"),
            ("latex string", r"\newpage"),
            ("QUESTION", "../tests/ciss240/a05/a05q01/question/main.tex"),
            ("latex string", r"\newpage"),
            ("QUESTION", "../tests/ciss240/a05/a05q02/question/main.tex"),
            ("latex string", r"\newpage"),
            ("QUESTION", "../tests/ciss240/a05/a05q03/question/main.tex"),
            ("latex string", r"\newpage"),
            ("QUESTION", "../tests/ciss240/a05/a05q04/question/main.tex")]
###########################################################################
