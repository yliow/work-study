curdir := $(notdir $(CURDIR))

# to create q0101.tar.gz
run:
	rm -rf $(curdir)
	rm -f $(curdir).tar.gz
	cd questions; make; rm -f main.aux main.idx main.log main.out makefile.old main.py main.py.err main.py.out latex.py submit.tar.gz; rm -rf submit
	cp -r questions $(curdir)
	tar -cvf $(curdir).tar $(curdir)
	#rm -rf $(curdir)
	gzip $(curdir).tar

c:
	rm -rf $(curdir)
	rm -f $(curdir).tar.gz

# to create answers
a:
	rm -rf answers
	mkdir answers
	cp -r questions/* answers/
	python parser.py
	cd answers; make
