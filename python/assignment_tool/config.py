courses = "ciss350"
ass = "a01"

dir = ["a01q01/question/main.tex", "a01q02/question/main.tex", "a01q03/question/main.tex"]

def makefile():
    make = '''pdf:\n\t-python /home/student/.alex/alexrunner.py replaceemail\n\tpdflatex --shell-escape
    main.tex\n\txdg-open main.pdf\nview:\n\txdg-open main.pdf\nv:\n\txdg-open main.pdf\ncleantmp:\n\trm
    -rf \'__pycache__\' \'auto\' \'desktop.ini\' \\\n\t\'abc.output\' \'texput.log\' \'shEsc.tmp\'\\ \n
    \t\'main.log\' \'main.aux\' \'main.toc\' \'main.out\' \'main.idx\' \'main.ilg\' \'main.vrb\' \'main.snm\'
    \'main.nav\' \\ \n\t\'main.py.err\' \'main.py.out\' \'main.py\' \'latex.py\' \'main.pytxcode\' \\ \n\t
    \'makefile.old\' \'missfont.log\' \'traceback.txt\'\nc:\n\tmake cleantmp\ns:\n\tmake cleantmp\n\n\t
    rm -rf submit; rm -f submit.tar.gz; mkdir submit; rsync -av . submit --exclude submit; tar -cvf submit.tar
    submit; gzip submit.tar || true\n\t@echo \"================================================================
    \"\n\t@echo \"done ... submit.tar.gz is created:\"\n\t@ls -la submit.tar.gz\n\t@echo \"
    ================================================================\"\n\t@echo \"\"'''
    return "makefile", make

def thismacros():
    tex = ""
    return "thismacros.tex", tex

def thispackages():
    tex = ""
    return "thispackages.tex", tex

def thispostamble():
    tex = "\\printindex\n\\end{document}"
    return "thispostamble.tex", tex

def thispreamble():
    tex = "\\newcommand\\COURSE{"
    tex = tex + courses
    tex = tex + "}\n\\newcommand\\ASSESSMENT{"
    tex = tex + ass
    tex = tex + '''}\n\\newcommand\\ASSESSMENTTYPE{Assignment}\n\\newcommand\\POINTS{\textwhite{xxx/xxx}}\n\n\\input{myquizpreamble}
    \n\\input{yliow}\n\\input{thistitle}\n\\renewcommand\\EMAIL{}\n\\input{\\COURSE}\n\\textwidth=6in\n\n\\input{thispackages}\n
    \\input{thismacros}\n\n\\makeindex\n\\begin{document}\n\\topmatter\n'''
    return "thispreamble.tex", tex

def thistitle():
    tex = "\\renewcommand\\TITLE{\\ASSESSMENTTYPE \\ \\ASSESSMENT}\n"
    return "thistitle.tex", tex

def write(x):
    name, s = x
    f = open(name, "w")
    f.write(s)
    f.close()
