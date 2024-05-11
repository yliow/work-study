curdir := $(notdir $(CURDIR))

run:
	cd questions; make; rm -f main.aux main.idx main.log main.out makefile.old main.py main.py.err main.py.out latex.py submit.tar.gz; rm -rf submit
	rm -rf $(curdir)
	rm -f $(curdir).tar.gz
	cp -r questions $(curdir)
	tar -cvf $(curdir).tar $(curdir)
	#rm -rf $(curdir)
	gzip $(curdir).tar
