#
# exercises/power-series-0????????
#

OPEN = xdg-open
PDF = pdflatex --shell-escape $@.tex; \
	pythontex $@.tex \
	pdflatex --shell-escape $@.tex; \
	makeindex $@.idx; \
	pdflatex --shell-escape $@.tex; \
	$(OPEN) $@.pdf; \
	echo ""; \
	ls -la $@.pdf; \
	echo ""

# chapter 11, page 11000
main: plot0.tex \
	plot1.tex \
	plot2.tex \
	plot3.tex \
	plot4.tex \
	plot5.tex \
	plot6.tex \
	plot7.tex \
	plot8.tex \
	plot9.tex \
	plot10.tex \
	plot11.tex \
	plot12.tex \
	plot13.tex \
	plot14.tex \
	test0.txt \
	exercises-recurrence-to-closed-form-0 \
	exercises-recurrence-to-closed-form-1 \
	exercises-tiling-0 \
	exercises-tiling-1 \
	exercises-tiling-2 \
	exercises-power-series-1 \
	exercises-power-series-2 \
	exercises-power-series-3 \
	exercises-power-series-4 \
	exercises-power-series-5 \
	exercises-power-series-6 \
	exercises-power-series-7 \
	exercises-power-series-8 \
	exercises-power-series-9
	$(PDF)

plot0.tex: plot0.py
	python plot0.py > plot0.tex
plot1.tex: plot1.py
	python plot1.py > plot1.tex
plot2.tex: plot2.py
	python plot2.py > plot2.tex
plot3.tex: plot3.py
	python plot3.py > plot3.tex
plot4.tex: plot4.py
	python plot4.py > plot4.tex
plot5.tex: plot5.py
	python plot5.py > plot5.tex
plot6.tex: plot6.py
	python plot6.py > plot6.tex
plot7.tex: plot7.py
	python plot7.py > plot7.tex
plot8.tex: plot8.py
	python plot8.py > plot8.tex
plot9.tex: plot9.py
	python plot9.py > plot9.tex
plot10.tex: plot10.py
	python plot10.py > plot10.tex
plot11.tex: plot11.py
	python plot11.py > plot11.tex
plot12.tex: plot12.py
	python plot12.py > plot12.tex
plot14.tex: plot14.py
	python plot14.py > plot14.tex

test0.txt: test0.py
	python test0.py > test0.txt

exercises-recurrence-to-closed-form-0:
	(cd exercises/recurrence-to-closed-form-0 && make)

exercises-recurrence-to-closed-form-1:
	(cd exercises/recurrence-to-closed-form-1 && make)

exercises-tiling-0:
	(cd exercises/tiling-0 && make)
exercises-tiling-1:
	(cd exercises/tiling-1 && make)
exercises-tiling-2:
	(cd exercises/tiling-2 && make)

exercises-power-series-1:
	(cd exercises/power-series-1 && make)
exercises-power-series-2:
	(cd exercises/power-series-2 && make)
exercises-power-series-3:
	(cd exercises/power-series-3 && make)
exercises-power-series-4:
	(cd exercises/power-series-4 && make)
exercises-power-series-5:
	(cd exercises/power-series-5 && make)
exercises-power-series-6:
	(cd exercises/power-series-6 && make)
exercises-power-series-7:
	(cd exercises/power-series-7 && make)
exercises-power-series-8:
	(cd exercises/power-series-8 && make)
exercises-power-series-9:
	(cd exercises/power-series-9 && make)

cleantmp:
	rm -rf abc.outut
	rm -rf '*.log' 
	rm -rf '*.aux'
	rm -rf '*.toc'
	rm -rf '*.out'
	rm -rf '*.idx'
	rm -rf '*.ilg'
	rm -rf '*.log'
	rm -rf 'shEsc.tmp'
	rm -rf '*.vrb'
	rm -rf '*.snm'
	rm -rf '*.nav'
	rm -rf '*.err'
	rm -rf '*.idx'
	rm -rf 'abc.output'


clean:
	rm -rf 'main.pdf'
	make cleantmp

c:
	rm -rf 'main.pdf'
	make cleantmp

mail:
	sendgmail --attach=*.pdf

v:
	$(OPEN) main.pdf
