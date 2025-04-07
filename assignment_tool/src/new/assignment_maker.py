from assignment_builder import *

questions = ["a02/Old/q01.tex",
             "a02/Old/q02.tex",
             "a02/Old/q03.tex"]

a = Assignment_Builder("ciss245",
                       "yliow", 2,
                       "Test",
                       len(questions))

a.add_extra_document("a02/Old/objectives.tex", True)
a.add_extra_document("a02/Old/instruction.tex", True)
a.add_latexstr(r"\newpage")
a.add_programming_question(questions[0])
a.add_skeleton("a02/Old/q01/main.cpp")
a.add_skeleton("a02/Old/q01/Fraction.h")
a.add_skeleton("a02/Old/q01/Fraction.cpp")
a.add_latexstr(r"\newpage")
a.add_programming_question(questions[1])
a.add_skeleton("a02/Old/q02/main.cpp")
a.add_skeleton("a02/Old/q02/Fraction.h")
a.add_skeleton("a02/Old/q02/Fraction.cpp")
a.add_latexstr(r"\newpage")
a.add_programming_question(questions[2])
a.add_skeleton("a02/Old/q03/Fraction.h")
a.add_skeleton("a02/Old/q03/Fraction.cpp")
a.build()

print(a.include_main_tex)

#---------------------------------------------------------------------------------
