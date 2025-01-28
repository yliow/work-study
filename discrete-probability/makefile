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

main: stdout/plot01.tex \
	stdout/plot02.tex \
	stdout/plot03.tex \
	stdout/plot04.tex \
	stdout/plot05.tex \
	stdout/plot06.tex \
	stdout/plot07.tex \
	stdout/stdout00.tex \
	stdout/stdout01.tex \
	stdout/stdout02.tex \
	stdout/stdout03.tex \
	stdout/stdout04.tex \
	stdout/stdout05.tex \
	stdout/stdout08a.tex \
	stdout/stdout08b.tex \
	stdout/stdout08c.tex \
	stdout/stdout09a.tex \
	stdout/stdout09b.tex \
	stdout/stdout10.tex 
	$(PDF)
	$(LATEXRM)
view:
	$(OPEN) main.pdf
v:
	$(OPEN) main.pdf

stdout/plot01.tex: stdout/plot01.py
	python stdout/plot01.py > stdout/plot01.tex
stdout/plot02.tex: stdout/plot02.py
	python stdout/plot02.py > stdout/plot02.tex
stdout/plot03.tex: stdout/plot03.py
	python stdout/plot03.py > stdout/plot03.tex
stdout/plot04.tex: stdout/plot04.py
	python stdout/plot04.py > stdout/plot04.tex
stdout/plot05.tex: stdout/plot05.py
	python stdout/plot05.py > stdout/plot05.tex
stdout/plot06.tex: stdout/plot06.py
	python stdout/plot06.py > stdout/plot06.tex
stdout/plot07.tex: stdout/plot07.py
	python stdout/plot07.py > stdout/plot07.tex
stdout/stdout00.tex: stdout/stdout00.py
	python stdout/stdout00.py > stdout/stdout00.tex
stdout/stdout01.tex: stdout/stdout01.py
	python stdout/stdout01.py > stdout/stdout01.tex
stdout/stdout02.tex: stdout/stdout02.py
	python stdout/stdout02.py > stdout/stdout02.tex
stdout/stdout03.tex: stdout/stdout03.py
	python stdout/stdout03.py > stdout/stdout03.tex
stdout/stdout04.tex: stdout/stdout04.py
	python stdout/stdout04.py > stdout/stdout04.tex
stdout/stdout05.tex: stdout/stdout05.py
	python stdout/stdout05.py > stdout/stdout05.tex
stdout/stdout08a.tex: stdout/stdout08a.py
	python stdout/stdout08a.py > stdout/stdout08a.tex
stdout/stdout08b.tex: stdout/stdout08b.py
	python stdout/stdout08b.py > stdout/stdout08b.tex
stdout/stdout08c.tex: stdout/stdout08c.py
	python stdout/stdout08c.py > stdout/stdout08c.tex
stdout/stdout09a.tex: stdout/stdout09a.py
	python stdout/stdout09a.py > stdout/stdout09a.tex
stdout/stdout09b.tex: stdout/stdout09b.py
	python stdout/stdout09b.py > stdout/stdout09b.tex
stdout/stdout10.tex: stdout/stdout10.py
	python stdout/stdout10.py > stdout/stdout10.tex

c:
	$(LATEXRM)	
