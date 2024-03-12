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

main: stdout00.tex stdout01.tex stdout02.tex stdout03.tex stdout04.tex stdout05.tex stdout06.tex stdout07.tex stdout08.tex stdout09.tex stdout10.tex stdout11.tex stdout12.tex stdout13.tex stdout14.tex stdout15.tex stdout16.tex stdout17.tex stdout18.tex stdout19.tex stdout20.tex stdout21.tex stdout22.tex stdout23.tex stdout24.tex stdout25.tex stdout26.tex
	$(PDF)
	$(LATEXRM)

c:
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

stdout09.tex: stdout09.py
	python stdout09.py > stdout09.tex

stdout10.tex: stdout10.py
	python stdout10.py > stdout10.tex

stdout11.tex: stdout11.py
	python stdout11.py > stdout11.tex

stdout12.tex: stdout12.py
	python stdout12.py > stdout12.tex

stdout13.tex: stdout13.py
	python stdout13.py > stdout13.tex

stdout14.tex: stdout14.py
	python stdout14.py > stdout14.tex

stdout15.tex: stdout15.py
	python stdout15.py > stdout15.tex

stdout16.tex: stdout16.py
	python stdout16.py > stdout16.tex

stdout17.tex: stdout17.py
	python stdout17.py > stdout17.tex

stdout18.tex: stdout18.py
	python stdout18.py > stdout18.tex

stdout19.tex: stdout19.py
	python stdout19.py > stdout19.tex

stdout20.tex: stdout20.py
	python stdout20.py > stdout20.tex

stdout21.tex: stdout21.py
	python stdout21.py > stdout21.tex

stdout22.tex: stdout22.py
	python stdout22.py > stdout22.tex

stdout23.tex: stdout23.py
	python stdout23.py > stdout23.tex

stdout24.tex: stdout24.py
	python stdout24.py > stdout24.tex

stdout25.tex: stdout25.py
	python stdout25.py > stdout25.tex

stdout26.tex: stdout26.py
	python stdout26.py > stdout26.tex
