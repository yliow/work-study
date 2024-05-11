curdir := $(notdir $(CURDIR))
run:
	cd questions; make; make c
	rm -rf $(curdir)
	rm -f $(curdir).tar.gz
	cp -r questions $(curdir)
	tar -cvf $(curdir).tar $(curdir)
	gzip $(curdir).tar
c:
	rm -rf $(curdir)
	rm -f $(curdir).tar.gz
	rm -rf __pycache__
a:
	rm -rf answers
	mkdir answers
	cp -r questions/* answers/
	python parser.py
	cd answers; make
