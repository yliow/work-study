import attributes as at
###########################################################################
#              THIS IS A TEMPLATE FOR THE "config.py" file!!
#              LOOK AT PDF TO DETERMINE THE STRUCTURE OF "config.py"
###########################################################################

#################################
#rename config to reflect assignment that has been generated using run.py
##################################################################
# depends on file structure
courses = "ciss245"
name = "yliow"
assignment = "a10"
assignment_it = "10";
basepath = "New/" # insert path for new directory (you are able to go back)
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
contents = [(at.OTHER, "Old/objectives.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.QUEST_CODE, "Old/q01.tex"),
            (at.LATEXSTR, r"\newpage"),
            (at.DOCUMENTS, "Old/instructions.tex"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram1.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram2.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram3.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram4.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram5.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram6.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram7.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram8.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram9.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram10.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram11.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram12.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram13.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram14.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram15.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram16.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram17.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram19.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram20.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram21.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram22.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram23.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram24.py"),
            (at.EXTRA_DOCUMENTS, "Old/diagrams/diagram25.py"),
            (at.LATEXSTR, r"\newpage"),
            (at.LATEXSTR, r'''\textsc{Test File}

The following is only a skeleton test code. Complete it and test your library thorougly.

{\small'''),
            (at.SKEL_PDF, "Old/testIntDynArr.cpp"),
            (at.LATEXSTR, r'''The test option numbering follows the same numbering as in the explanation earlier.''')
            ]
###########################################################################
