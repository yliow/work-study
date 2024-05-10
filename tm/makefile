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

stdout06.tex:
	python stdout06.py > stdout06.tex

stdout07.tex:
	python stdout07.py > stdout07.tex

stdout08.tex:
	python stdout08.py > stdout08.tex

stdout09.tex:
	python stdout09.py > stdout09.tex

stdout10.tex:
	python stdout10.py > stdout10.tex

stdout11.tex:
	python stdout11.py > stdout11.tex

stdout12.tex:
	python stdout12.py > stdout12.tex

stdout13.tex:
	python stdout13.py > stdout13.tex

stdout14.tex:
	python stdout14.py > stdout14.tex

stdout15.tex:
	python stdout15.py > stdout15.tex

stdout16.tex:
	python stdout16.py > stdout16.tex

stdout17.tex:
	python stdout17.py > stdout17.tex

stdout18.tex:
	python stdout18.py > stdout18.tex

stdout19.tex:
	python stdout19.py > stdout19.tex

stdout20.tex:
	python stdout20.py > stdout20.tex

stdout21.tex:
	python stdout21.py > stdout21.tex

stdout22.tex:
	python stdout22.py > stdout22.tex

stdout23.tex:
	python stdout23.py > stdout23.tex

stdout24.tex:
	python stdout24.py > stdout24.tex

stdout25.tex:
	python stdout25.py > stdout25.tex

stdout26.tex:
	python stdout26.py > stdout26.tex
