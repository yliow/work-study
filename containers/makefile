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
c:
	$(LATEXRM)
view:
	$(OPEN) main.pdf
v:
	$(OPEN) main.pdf
