
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
	-rf '__pycache__' 'auto' 'desktop.ini' 	'abc.output' 'texput.log' 'shEsc.tmp'	'main.log' 'main.aux' 'main.toc' 'main.out' 'main.idx' 'main.ilg' 'main.vrb' 'main.snm' 'main.nav' 	'main.py.err' 'main.py.out' 'main.py' 'latex.py' 'main.pytxcode' 	'makefile.old' 'missfont.log' 'traceback.txt'
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

t tree :
	tree a06q01/ a06q02/ a06q03/ a06q04/ a06q05/ a06q06/ a06q07/ a06q08/ a06q09/ a06q10/ a06q11/ a06q12/ a06q13/ a06q14/ a06q15/ a06q16/ a06q17/ a06q18/ a06q19/ a06q20/