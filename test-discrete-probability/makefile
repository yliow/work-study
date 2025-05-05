OPEN = xdg-open
PDF = rm -rf solutions; touch solutions.tex; \
	pdflatex --shell-escape -halt-on-error -interaction=nonstopmode -file-line-error $@.tex && \
	pdflatex --shell-escape $@.tex && \
	pdflatex --shell-escape $@.tex && \
	pythontex main.tex && \
        makeindex $@.idx && \
        pdflatex --shell-escape $@.tex && \
        $(OPEN) $@.pdf;
LATEXRM = rm -f \
        main.aux main.ilg main.log main.idx main.ind main.out \
        main.py.err main.py.out \
        comment.cut comment.err comment.out \
        latex.py

main: 	
	$(PDF)
	$(LATEXRM)
view:
	$(OPEN) main.pdf
v:
	$(OPEN) main.pdf

disc/stdout/stdout11.tex: disc/stdout/stdout11.py
	python disc/stdout/stdout11.py > disc/stdout/stdout11.tex
disc/stdout/stdout12.tex: disc/stdout/stdout12.py
	python disc/stdout/stdout12.py > disc/stdout/stdout12.tex
disc/stdout/stdout13.tex: disc/stdout/stdout13.py
	python disc/stdout/stdout13.py > disc/stdout/stdout13.tex
disc/stdout/stdout14.tex: disc/stdout/stdout14.py
	python disc/stdout/stdout14.py > disc/stdout/stdout14.tex
disc/stdout/stdout15.tex: disc/stdout/stdout15.py
	python disc/stdout/stdout15.py > disc/stdout/stdout15.tex
disc/stdout/stdout16.tex: disc/stdout/stdout16.py
	python disc/stdout/stdout16.py > disc/stdout/stdout16.tex
disc/stdout/stdout17.tex: disc/stdout/stdout17.py
	python disc/stdout/stdout17.py > disc/stdout/stdout17.tex
disc/stdout/stdout00.tex: disc/stdout/stdout00.py
	python disc/stdout/stdout00.py > disc/stdout/stdout00.tex
disc/stdout/stdout01.tex: disc/stdout/stdout01.py
	python disc/stdout/stdout01.py > disc/stdout/stdout01.tex
disc/stdout/stdout02.tex: disc/stdout/stdout02.py
	python disc/stdout/stdout02.py > disc/stdout/stdout02.tex
disc/stdout/stdout03.tex: disc/stdout/stdout03.py
	python disc/stdout/stdout03.py > disc/stdout/stdout03.tex
disc/stdout/stdout04.tex: disc/stdout/stdout04.py
	python disc/stdout/stdout04.py > disc/stdout/stdout04.tex
disc/stdout/stdout05.tex: disc/stdout/stdout05.py
	python disc/stdout/stdout05.py > disc/stdout/stdout05.tex
disc/stdout/stdout08a.tex: disc/stdout/stdout08a.py
	python disc/stdout/stdout08a.py > disc/stdout/stdout08a.tex
disc/stdout/stdout08b.tex: disc/stdout/stdout08b.py
	python disc/stdout/stdout08b.py > disc/stdout/stdout08b.tex
disc/stdout/stdout08c.tex: disc/stdout/stdout08c.py
	python disc/stdout/stdout08c.py > disc/stdout/stdout08c.tex
disc/stdout/stdout09a.tex: disc/stdout/stdout09a.py
	python disc/stdout/stdout09a.py > disc/stdout/stdout09a.tex
disc/stdout/stdout09b.tex: disc/stdout/stdout09b.py
	python disc/stdout/stdout09b.py > disc/stdout/stdout09b.tex
disc/stdout/stdout10.tex: disc/stdout/stdout10.py
	python disc/stdout/stdout10.py > disc/stdout/stdout10.tex

c:
	$(LATEXRM)	
