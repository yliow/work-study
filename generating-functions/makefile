#
# exercises/power-series-0????????
#

OPEN = xdg-open
PDF = pdflatex --shell-escape $@.tex; \
	pythontex $@.tex \
	makeindex $@.idx; \
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
	exercises-power-series-9 \
	stdout00.tex \
	stdout01.tex \
	stdout02.tex \
	stdout03.tex \
	stdout04.tex \
	stdout05.tex \
	stdout06.tex \
	stdout07.tex \
	stdout08.tex \
	stdout09.tex \
	stdout10.tex \
	stdout11.tex \
	stdout12.tex \
	stdout13.tex \
	stdout14.tex \
	stdout15.tex \
	stdout16.tex \
	stdout17.tex \
	stdout18.tex \
	stdout19.tex \
	stdout20.tex \
	stdout21.tex \
	stdout22.tex \
	stdout23.tex \
	stdout24.tex \
	stdout25.tex \
	stdout26.tex \
	stdout27.tex \
	stdout28.tex \
	stdout29.tex \
	stdout30.tex \
	stdout31.tex \
	stdout32.tex \
	stdout33.tex \
	stdout34.tex
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
	rm -rf *.log
	rm -rf *.aux
	rm -rf *.toc
	rm -rf *.out
	rm -rf *.idx
	rm -rf *.ilg
	rm -rf *.log
	rm -rf shEsc.tmp
	rm -rf *.vrb
	rm -rf *.snm
	rm -rf *.nav
	rm -rf *.err
	rm -rf *.idx
	rm -rf abc.output


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
