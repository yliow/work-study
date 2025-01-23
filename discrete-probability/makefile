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

main: plot01.tex \
	plot02.tex \
	plot03.tex \
	plot04.tex \
	plot05.tex \
	plot06.tex \
	plot07.tex \
	stdout00.tex \
	stdout01.tex \
	stdout02.tex \
	stdout03.tex \
	stdout04.tex \
	stdout05.tex \
	stdout08a.tex \
	stdout08b.tex \
	stdout08c.tex \
	stdout09a.tex \
	stdout09b.tex \
	stdout10.tex 
	$(PDF)
	$(LATEXRM)
view:
	$(OPEN) main.pdf
v:
	$(OPEN) main.pdf

plot01.tex: plot01.py
	python plot01.py > plot01.tex
plot02.tex: plot02.py
	python plot02.py > plot02.tex
plot03.tex: plot03.py
	python plot03.py > plot03.tex
plot04.tex: plot04.py
	python plot04.py > plot04.tex
plot05.tex: plot05.py
	python plot05.py > plot05.tex
plot06.tex: plot06.py
	python plot06.py > plot06.tex
plot07.tex: plot07.py
	python plot07.py > plot07.tex
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
stdout08a.tex: stdout08a.py
	python stdout08a.py > stdout08a.tex
stdout08b.tex: stdout08b.py
	python stdout08b.py > stdout08b.tex
stdout08c.tex: stdout08c.py
	python stdout08c.py > stdout08c.tex
stdout09a.tex: stdout09a.py
	python stdout09a.py > stdout09a.tex
stdout09b.tex: stdout09b.py
	python stdout09b.py > stdout09b.tex
stdout10.tex: stdout10.py
	python stdout10.py > stdout10.tex

c:
	$(LATEXRM)	
