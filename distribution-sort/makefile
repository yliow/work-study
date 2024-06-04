OPEN = xdg-open
PDF = pdflatex --shell-escape $@.tex; \
        makeindex $@.idx; \
        pdflatex --shell-escape $@.tex; \
        $(OPEN) $@.pdf; 
LATEXRM = rm -f \
        main.aux main.ilg main.log main.idx main.ind main.out \
        main.py.err main.py.out \
        comment.cut comment.err comment.out \
        latex.py

main: stdout00.tex stdout01.tex stdout02.tex stdout03.tex stdout04.tex stdout05.tex stdout06.tex stdout07.tex stdout08.tex
	$(PDF)
	$(LATEXRM)
view:
	$(OPEN) main.pdf
v:
	$(OPEN) main.pdf

stdout00.tex: stdout00.py
	python stdout00.py > stdout00.tex

stdout01.tex: stdout01.py
	python stdout01.py > stdout01.tex

stdout02.tex: stdout02.py
	python stdout02.py > stdout02.tex

stdout03.tex: stdout03.py
	python stdout03.py > stdout03.tex

stdout04.tex: stdout04.py
	python stdout04.py > stdout04.tex

stdout05.tex: stdout05.py
	python stdout05.py > stdout05.tex

stdout06.tex: stdout06.py
	python stdout06.py > stdout06.tex

stdout07.tex: stdout07.py
	python stdout07.py > stdout07.tex

stdout08.tex: stdout08.py
	python stdout08.py > stdout08.tex
