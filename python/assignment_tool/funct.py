from math import *
import config

def makefile():
    make = '''
pdf:
	-python /home/student/.alex/alexrunner.py replaceemail
	pdflatex --shell-escape main.tex
	xdg-open main.pdf
view:
	xdg-open main.pdf
v:
	xdg-open main.pdf
cleantmp:
	rm
	-rf '__pycache__' 'auto' 'desktop.ini' \
	'abc.output' 'texput.log' 'shEsc.tmp'\
	'main.log' 'main.aux' 'main.toc' 'main.out' 'main.idx' 'main.ilg' 'main.vrb' 'main.snm' 'main.nav' \
	'main.py.err' 'main.py.out' 'main.py' 'latex.py' 'main.pytxcode' \
	'makefile.old' 'missfont.log' 'traceback.txt'
c:
	make cleantmp
s:
	make cleantmp
	rm -rf submit; rm -f submit.tar.gz; mkdir submit; rsync -av . submit --exclude submit; tar -cvf submit.tar
	submit; gzip submit.tar || true
	@echo "================================================================"
	@echo "done ... submit.tar.gz is created:"
	@ls -la submit.tar.gz
	@echo "================================================================"
	@echo ""

    '''
    return "makefile", make


def thispostamble():
    tex = "\\printindex\n\\end{document}"
    return "thispostamble.tex", tex

def thispreamble():
    tex = r'''\newcommand\COURSE{%(courses)s}
\newcommand\ASSESSMENT{%(assignment)s}
\newcommand\ASSESSMENTTYPE{Assignment}
\newcommand\POINTS{	extwhite{xxx/xxx}}

\input{myquizpreamble}
    
\input{%(name)s}
\input{thistitle}
\renewcommand\EMAIL{}
\input{\COURSE}
\textwidth=6in

\input{thispackages}
    
    \input{thismacros}

\makeindex
\begin{document}
\topmatter
    ''' % {'assignment': config.assignment,
        'courses': config.courses,
        'name':config.name}
    return "thispreamble.tex", tex

def thistitle():
    tex = r'''\renewcommand\TITLE{\ASSESSMENTTYPE \ \ASSESSMENT}
    '''
    return "thistitle.tex", tex

def write(x):
    name, s = x
    f = open(name, "w")
    f.write(s)
    f.close()

def is_latex(path):
    x = path[len(path) - 4:len(path)]
    return x == '.tex'
   
def include_latex(path):
    tex = r'''\input{%(path)s}''' %{'path':path}
    return tex

def include_src(path, frame='single', fontsize='\\footnotesize'):
    src = r'''\VerbatimInput[frame=%(frame)s,font=%(fontsize)s]{%(path)s}
    ''' % {'path':path, 'frame':frame, 'fontsize':fontsize}
    return src

def include_(path):
    if is_latex(path):
        return include_latex(path)
    else:
        return include_src(path)
     
    
