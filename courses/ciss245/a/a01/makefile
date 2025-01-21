run:
	make copy; python *.py; make clean
copy:
	cp ../../../../assignment_tool/src/attributes.py .; cp ../../../../assignment_tool/src/makefile.py .; cp ../../../../assignment_tool/src/mk_assignment.py .; cp ../../../../assignment_tool/src/file_structure.py .; cp ../../../../assignment_tool/src/latex_fragment.py .; cp ../../../../assignment_tool/src/tarzip.py .

clean:
	rm attributes.py; rm mk_assignment.py; rm makefile.py; rm file_structure.py; rm latex_fragment.py; rm tarzip.py
	rm -r __pycache__


tarzip tz:
	tar -cvf New/a01.tar New/a01
	gzip New/a01.tar;
