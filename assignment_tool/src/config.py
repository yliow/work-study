

###########################################################################
#              THIS IS A TEMPLATE FOR THE "config.py" file!!
#              LOOK AT PDF TO DETERMINE THE STRUCTURE OF "config.py"
###########################################################################

# depends on file structure
name = "yliow"
courses = "ciss350"

assignment = "a04"

num = 4

#TODO
#co

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
contents = [("latex string", r"\newpage"),
            ("QUESTION", "../tests/ciss240/a01/a01q01/question/main.tex"),
            ("latex string", r"\newpage"),
            ("QUESTION", "../tests/ciss240/a01/a01q02/question/main.tex"),
            ("latex string", r"\newpage"),
            ("QUESTION", "../tests/ciss240/a01/a01q03/question/main.tex")]
###########################################################################
