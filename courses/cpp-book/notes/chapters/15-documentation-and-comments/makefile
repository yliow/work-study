LATEXRM = rm -f \
        main.aux main.ilg main.log main.idx main.ind main.out \
        main.py.err main.py.out \
        comment.cut comment.err comment.out main.pytxcode \
        latex.py
compile c:
	pdflatex main.tex ;
	pdflatex main.tex ;
	make o
m:
	nvim makefile
p:
	open 15-documentation-and-comments.pdf
e:
	nvim main.tex
o:
	open main.pdf
c:
	$(LATEXRM)

