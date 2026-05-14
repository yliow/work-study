pdf:
	pdflatex --shell-escape main.tex
v:
	xdg-open main.pdf
clean:
	rm -rf abc.outut
	rm -rf 'main.log' 
	rm -rf 'main.aux'
	rm -rf 'main.toc'
	rm -rf 'main.out'
	rm -rf 'main.idx'
	rm -rf 'main.ilg'
	rm -rf 'texput.log'
	rm -rf 'shEsc.tmp'
	rm -rf 'main.vrb'
	rm -rf 'main.snm'
	rm -rf 'main.nav'
	rm -rf 'abc.output'
	rm -rf comment.* latex.py main.py main.py.err main.py.out main.pytxcode
c:
	make clean
cc:
	rm -rf 'main.pdf'
	make clean
