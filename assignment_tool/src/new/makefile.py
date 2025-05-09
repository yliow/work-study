import os

def maketree(num, assignment):
    s = '''
t tree :
	tree'''
    for i in range(1, num + 1):
        s += rf" {assignment}q{i:0>2}/"
    return s

def makefile(num, assignment):
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
%s'''% maketree(num, assignment)#CLEANUP
    return "makefile", make
