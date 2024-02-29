OPEN = xdg-open
PDF = rm -rf solutions; touch solutions.tex; \
	pdflatex --shell-escape -halt-on-error -interaction=nonstopmode -file-line-error $@.tex && \
	pythontex main.tex && \
        makeindex $@.idx && \
        pdflatex --shell-escape $@.tex && \
        $(OPEN) $@.pdf;
LATEXRM = rm -f \
        main.aux main.ilg main.log main.idx main.ind main.out \
        main.py.err main.py.out \
        comment.cut comment.err comment.out \
        latex.py

main:  stdout00.tex stdout01.tex stdout02.tex stdout03.tex stdout04.tex stdout05.tex stdout06.tex stdout07.tex stdout08.tex stdout09.tex stdout10.tex stdout11.tex stdout12.tex stdout13.tex stdout14.tex stdout15.tex stdout16.tex stdout17.tex stdout18.tex stdout19.tex stdout20.tex stdout21.tex stdout22.tex stdout23.tex stdout24.tex stdout25.tex stdout26.tex stdout27.tex stdout28.tex stdout29.tex stdout30.tex stdout31.tex stdout32.tex stdout33.tex stdout34.tex stdout35.tex stdout36.tex stdout37.tex stdout38.tex stdout39.tex stdout40.tex stdout41.tex stdout42.tex stdout43.tex stdout44.tex stdout45.tex stdout46.tex stdout47.tex stdout48.tex stdout49.tex stdout50.tex stdout51.tex stdout52.tex stdout53.tex stdout54.tex stdout55.tex stdout56.tex stdout57.tex stdout58.tex stdout59.tex stdout60.tex stdout61.tex
	$(PDF)
	$(LATEXRM)
view:
	$(OPEN) main.pdf
v:
	$(OPEN) main.pdf
c:
	$(LATEXRM)

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

stdout27.tex: stdout27.py
	python stdout27.py > stdout27.tex

stdout28.tex: stdout28.py
	python stdout28.py > stdout28.tex

stdout29.tex: stdout29.py
	python stdout29.py > stdout29.tex

stdout30.tex: stdout30.py
	python stdout30.py > stdout30.tex

stdout31.tex: stdout31.py
	python stdout31.py > stdout31.tex

stdout32.tex: stdout32.py
	python stdout32.py > stdout32.tex

stdout33.tex: stdout33.py
	python stdout33.py > stdout33.tex

stdout34.tex: stdout34.py
	python stdout34.py > stdout34.tex

stdout35.tex: stdout35.py
	python stdout35.py > stdout35.tex

stdout36.tex: stdout36.py
	python stdout36.py > stdout36.tex

stdout37.tex: stdout37.py
	python stdout37.py > stdout37.tex

stdout38.tex: stdout38.py
	python stdout38.py > stdout38.tex

stdout39.tex: stdout39.py
	python stdout39.py > stdout39.tex

stdout40.tex: stdout40.py
	python stdout40.py > stdout40.tex

stdout41.tex: stdout41.py
	python stdout41.py > stdout41.tex

stdout42.tex: stdout42.py
	python stdout42.py > stdout42.tex

stdout43.tex: stdout43.py
	python stdout43.py > stdout43.tex

stdout44.tex: stdout44.py
	python stdout44.py > stdout44.tex

stdout45.tex: stdout45.py
	python stdout45.py > stdout45.tex

stdout46.tex: stdout46.py
	python stdout46.py > stdout46.tex

stdout47.tex: stdout47.py
	python stdout47.py > stdout47.tex

stdout48.tex: stdout48.py
	python stdout48.py > stdout48.tex

stdout49.tex: stdout49.py
	python stdout49.py > stdout49.tex

stdout50.tex: stdout50.py
	python stdout50.py > stdout50.tex

stdout51.tex: stdout51.py
	python stdout51.py > stdout51.tex

stdout52.tex: stdout52.py
	python stdout52.py > stdout52.tex

stdout53.tex: stdout53.py
	python stdout53.py > stdout53.tex

stdout54.tex: stdout54.py
	python stdout54.py > stdout54.tex

stdout55.tex: stdout55.py
	python stdout55.py > stdout55.tex

stdout56.tex: stdout56.py
	python stdout56.py > stdout56.tex

stdout57.tex: stdout57.py
	python stdout57.py > stdout57.tex

stdout58.tex: stdout58.py
	python stdout58.py > stdout58.tex

stdout59.tex: stdout59.py
	python stdout59.py > stdout59.tex

stdout60.tex: stdout60.py
	python stdout60.py > stdout60.tex

stdout61.tex: stdout61.py
	python stdout61.py > stdout61.tex
