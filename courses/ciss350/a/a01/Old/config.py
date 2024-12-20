courses = "ciss350"
assignment = "a01"

dir = ["a01q01/question/main.tex",
       "a01q02/question/main.tex",
       "a01q03/question/main.tex"]

def include_tex():
    input  = "\\VerbatimInput"
def include_src():
    
    
def write(x):
    name, s = x
    f = open(name, "w")
    f.write(s)
    f.close()
