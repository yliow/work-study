run:
	rm -f a05.tar.gz
	rm -rf a05
	mkdir a05
	cp -r questions/* a05/
	cd a05/; rm -rf main.aux main.idx main.log main.out makefile.old main.py main.py.err main.py.out latex.py a.out __pycache__
	tar -cvf a05.tar a05
	gzip a05.tar


