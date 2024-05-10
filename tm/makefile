OPEN = xdg-open
PDF = pdflatex --shell-escape $@.tex; \
        $(OPEN) $@.pdf; 
LATEXRM = rm -f \
        main.aux main.ilg main.log main.idx main.ind main.out \
        main.py.err main.py.out \
        comment.cut comment.err comment.out \
				latex.py

main: stdout00.tex stdout01.tex stdout02.tex stdout03.tex stdout04.tex stdout05.tex 
	$(PDF)
	$(LATEXRM)
view:
	$(OPEN) main.pdf
v:
	$(OPEN) main.pdf

c:
	$(LATEXRM)

stdout00.tex:
	python stdout00.py > stdout00.tex

stdout01.tex:
	python stdout01.py > stdout01.tex

stdout02.tex:
	python stdout02.py > stdout02.tex

stdout03.tex:
	python stdout03.py > stdout03.tex

stdout04.tex:
	python stdout04.py > stdout04.tex

stdout05.tex:
	python stdout05.py > stdout05.tex
